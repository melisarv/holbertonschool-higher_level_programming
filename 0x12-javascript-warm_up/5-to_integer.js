#!/usr/bin/node
const argv = process.argv[2];
if (isNaN(argv)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(argv));
}
