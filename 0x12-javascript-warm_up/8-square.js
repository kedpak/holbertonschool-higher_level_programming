#!/usr/bin/node
// Write a script that prints a square
// The first argument is the size of the square
// You must use the character X to print the square
let args = process.argv.slice(2);

if (isNaN(args[0]) === true) {
  console.log('Missing size');
}
let list = [];
for (let i = 0; i < Number(args[0]); i++) {
  for (let j = 0; j < Number(args[0]); j++) {
    list.push('X');
  }
  let xPrint = list.join('');
  console.log(xPrint);
  list = [];
}
