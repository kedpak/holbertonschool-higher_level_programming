#!/usr/bin/node
// Write a script that prints the addition of 2 integers
// The first argument is the first integer, second arg second integer
let args = process.argv.slice(2);

function add (a, b) {
  console.log(Number(a) + Number(b));
}
add(args[0], args[1]);
