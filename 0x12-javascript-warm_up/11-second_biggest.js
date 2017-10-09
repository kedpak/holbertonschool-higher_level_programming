#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.
let args = process.argv.slice(2);

let max = Number(args[0]);
let second = max;

if (args.length === 0 || args.length === 1) {
  second = 0;
} else {
  for (let i = 0; i < args.length; i++) {
    if (Number(args[i]) > max) {
      max = Number(args[i]);
    }
  }
  for (let j = 0; j < args.length; j++) {
    if (Number(args[j]) === max) {
      continue;
    }
    if (Number(args[0]) === max) {
      second = Number(args[1]);
    }
    if (Number(args[j]) > second) {
      second = Number(args[j]);
    }
  }
}
console.log(second);
