#!/usr/bin/node

const requist = require('request');
const ur = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];
requist.get(ur + id, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
