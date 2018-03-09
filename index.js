const express = require('express');
const cors = require('cors');
const mysql = require('mysql')
const selectAll = 'SELECT * FROM companies';
const app = express();
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'Inc5000',
});

connection.connect(err => {
  if(err){
    return err;
  }
});


app.use(cors());

app.get('/', (req, res) => {
  res.send('Mira RAMON estoy conectando una base de datos sql XXX con nodejs!')
});

app.listen(3000, () => {
  console.log('Inc5000 server listening on port');
})
