#!/usr/bin/node

let args = process.argv.slice(2);

if (isNaN(args[0]) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(args); i++) {
    console.log('C is fun');
  }
}
