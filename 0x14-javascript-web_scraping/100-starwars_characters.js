#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) { console.log(error); }
  const characters = JSON.parse(body).characters;
  characters.forEach((character) => {
    request(character, function (error, responde, body) {
      if (error) { console.log(error); }
      console.log(JSON.parse(body).name);
    });
  });
});
