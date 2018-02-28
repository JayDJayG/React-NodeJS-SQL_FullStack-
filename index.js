const express = require('express');
const cors = require('cors');

const app = express();

app.use(cors());

app.listen(4000, () => {
  console.log('Inc5000 server listening on port');
})
