import worker from '../src/worker.js';

export default async function handler(req, res) {
  // Convert Node/Vercel request to standard Fetch Request
  const protocol = req.headers['x-forwarded-proto'] || 'https';
  const host = req.headers['x-forwarded-host'] || req.headers.host || 'localhost';
  const fullUrl = `${protocol}://${host}${req.url}`;
  
  const headers = new Headers();
  for (const [key, val] of Object.entries(req.headers)) {
    if (val) headers.set(key, Array.isArray(val) ? val.join(', ') : val);
  }

  const fetchRequest = new Request(fullUrl, {
    method: req.method,
    headers: headers,
    body: (req.method !== 'GET' && req.method !== 'HEAD') ? JSON.stringify(req.body) : undefined
  });

  const workerResponse = await worker.fetch(fetchRequest, {}, {});
  
  res.status(workerResponse.status);
  workerResponse.headers.forEach((val, key) => {
    res.setHeader(key, val);
  });
  
  const bodyText = await workerResponse.text();
  res.send(bodyText);
}
