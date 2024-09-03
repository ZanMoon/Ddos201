const express = require('express');
const app = express();
const port = 8080;

// Middleware to parse JSON bodies
app.use(express.json());

const key = "@lizardpredator";

// Endpoint untuk memulai serangan
app.post('/api/start-attack', (req, res) => {
  try {
    const { keyFromQuery, host, port, time, method } = req.body;

    if (keyFromQuery !== key) {
      return res.status(401).send('Key not working');
    }

    if (!host || isNaN(port) || isNaN(time) || method !== 'TCP') {
      return res.status(400).send('Invalid parameters or method');
    }

    console.log(`Starting attack on ${host}:${port} for ${time}ms using method ${method}`);

    // Logika untuk memulai serangan bisa ditambahkan di sini

    // Respon berhasil
    res.status(200).send(`Attack started on ${host}:${port} for ${time}ms`);
  } catch (error) {
    console.error(error);
    res.status(500).send('There was a problem.');
  }
});

app.listen(port, () => {
  console.log(`API LizardC2 Started on port ${port}`);
});
