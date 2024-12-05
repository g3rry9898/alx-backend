import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.connect();

function createHash() {
  client.hset('ALX', 'Portland', 50, print);
  client.hset('ALX', 'Seattle', 80, print);
  client.hset('ALX', 'New York', 20, print);
  client.hset('ALX', 'Bogota', 20, print);
  client.hset('ALX', 'Cali', 40, print);
  client.hset('ALX', 'Paris', 2, print);
}

function displayHash() {
  client.hgetall('ALX', (err, obj) => {
    if (err) {
      console.error(`Error retrieving hash: ${err.message}`);
    } else {
      console.log(obj);
    }
  });
}

// Call the functions as specified
createHash();
displayHash();

