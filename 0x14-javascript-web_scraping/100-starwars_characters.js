#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
req.get(url + id, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const ff = data.characters;
  for (const j of ff) {
    req.get(j, function (err, response, bo1) {
      if (err) {
        console.log(err);
      }
      const info1 = JSON.parse(bo1);
      console.log(info1.name);
    });
  }
});
