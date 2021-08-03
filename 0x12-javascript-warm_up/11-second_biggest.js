#!/usr/bin/node

const argv = process.argv;
if (argv.length < 4) {
  console.log(0);
} else {
  console.log(argv.sort().reverse()[1]);
}
