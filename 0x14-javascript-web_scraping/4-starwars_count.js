#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) { console.log(error); }
  const results = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < results.length; i++) {
    const characters = results[i].characters;
    for (let j = 0; j < characters.length; j++) {
      if (characters[j].includes('18')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
