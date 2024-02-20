#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, res, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, i) {
  request(characters[i], function (err, res, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (i + 1 < characters.length) {
        printCharacters(characters, i + 1);
      }
    }
  });
}
