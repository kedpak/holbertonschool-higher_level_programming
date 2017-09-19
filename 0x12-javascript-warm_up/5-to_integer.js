#!/usr/bin/node

let args = process.argv.slice(2);
for (let i = 0; i < args.length; i++) {
  if (isNaN(Number(args[i])) === true) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + Number(args[i]));
  }
}
