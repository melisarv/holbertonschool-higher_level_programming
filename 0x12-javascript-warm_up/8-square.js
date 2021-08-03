#!/usr/bin/node
const argv = process.argv[2];
if (isNaN(argv)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv; i++) {
    console.log('X'.repeat(argv));
  }
}
