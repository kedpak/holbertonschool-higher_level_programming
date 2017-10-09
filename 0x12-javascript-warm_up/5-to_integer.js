#!/usr/bin/node
// Write a script that prints “My number: ” 
// if the first argument can be converted to an integer
// If the argument can’t be converted to an integer, print “Not a number”
let args = process.argv.slice(2);
for (let i = 0; i < args.length; i++) {
  if (isNaN(Number(args[i])) === true) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + Number(args[i]));
  }
}
