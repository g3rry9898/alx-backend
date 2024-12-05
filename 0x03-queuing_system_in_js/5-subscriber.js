import { createClient } from 'redis';

const subscriber = createClient();

subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

subscriber.connect();

subscriber.subscribe('ALXchannel', (err, count) => {
  if (err) {
    console.error(`Failed to subscribe: ${err.message}`);
  } else {
    console.log(`Subscribed successfully! This client is currently subscribed to ${count} channels.`);
  }
});

subscriber.on('message', (channel, message) => {
  console.log(`Received message from ${channel}: ${message}`);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});

