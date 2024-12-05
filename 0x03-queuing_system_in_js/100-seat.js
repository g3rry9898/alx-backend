import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';
import kue from 'kue';

const app = express();
const port = 1245;

const client = createClient();
client.on('error', (err) => console.error(`Redis client not connected to the server: ${err.message}`));
client.connect();

const reserveSeat = (number) => {
  client.set('available_seats', number);
};

const getAsync = promisify(client.get).bind(client);

async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return seats ? parseInt(seats, 10) : 0;
}

let reservationEnabled = true;
reserveSeat(50);

const queue = kue.createQueue();

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  }).on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentSeats = await getCurrentAvailableSeats();

    if (currentSeats <= 0) {
      reservationEnabled = false;
      return done(new Error('Not enough seats available'));
    }

    reserveSeat(currentSeats - 1);
    if (currentSeats - 1 === 0) {
      reservationEnabled = false;
    }
    done();
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

