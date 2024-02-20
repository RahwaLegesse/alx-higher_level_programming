#!/usr/bin/node
const fs = require('fs');
const f = process.argv[2];
const cont = process.argv[3];
fs.writeFile(f, cont, 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});
