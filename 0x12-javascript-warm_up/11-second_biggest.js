#!/usr/bin/node
let argv = process.argv;
if (argv.length < 4) {
  console.log(0);
} else {
  argv = argv.slice(2);
  argv.sort();
  console.log(argv[argv.length - 2]);
}
