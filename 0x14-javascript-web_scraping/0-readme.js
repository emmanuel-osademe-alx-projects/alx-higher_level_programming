#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  (err) ? console.log(err) : console.log(data);
});
