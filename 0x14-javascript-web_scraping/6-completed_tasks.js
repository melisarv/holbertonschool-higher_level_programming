#!/usr/bin/node
// computes the number of tasks completed by user id
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) { console.log(error); }
  const todos = JSON.parse(body);
  const done = {};
  for (const i of todos) {
    if (i.completed === true) {
      if (i.userId in done) {
        done[i.userId] += 1;
      } else {
        done[i.userId] = 1;
      }
    }
  }
  console.log(done);
});
