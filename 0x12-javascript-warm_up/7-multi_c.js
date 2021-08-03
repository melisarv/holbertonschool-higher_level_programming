#!/usr/bin/node
const argv = process.argv[2];
if (isNaN(argv)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argv; i++) {
    console.log('C is fun');
  }
}
