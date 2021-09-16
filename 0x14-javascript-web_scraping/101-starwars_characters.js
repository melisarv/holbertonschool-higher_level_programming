#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) console.log(error);
  else {
    const characters = JSON.parse(body).characters;
    const list = [];
    for (const character in characters) {
      const promise = new Promise(resolve => {
        request(characters[character], function (error, responde, body) {
          if (error) console.log(error);
          else {
            resolve(JSON.parse(body).name);
          }
        });
      });
      list.push(promise);
    }
    Promise.all(list).then(function (namelist) {
      for (const n in namelist) {
        console.log(namelist[n]);
      }
    });
  }
});
