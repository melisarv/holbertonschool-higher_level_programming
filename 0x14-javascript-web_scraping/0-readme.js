#!/usr/bin/node
// script that reads and prints the content of a file
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function read (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
