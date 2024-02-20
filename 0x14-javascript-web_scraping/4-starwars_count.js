#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (!err) {
    const resu = JSON.parse(body).resu;
    console.log(resu.reduce((c, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? c + 1
        : c;
    }, 0));
  }
});
