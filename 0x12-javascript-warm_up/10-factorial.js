#!/usr/bin/node
// Write a script that computes and prints a factorial
// The first argument is integer used for computing the factorial
// Factorial of NaN is 1
let args = process.argv.slice(2);

function factorial (num) {
  if (isNaN(num) === true || num <= 0) {
    return (1);
  } else {
    return (Number(num) * factorial(Number(num) - 1));
  }
}

console.log(factorial(args[0]));
