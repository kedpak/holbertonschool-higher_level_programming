#!/usr/bin/node

let args = process.argv.slice(2);

function factorial (num) {
  if (isNaN(num) === true || num <= 0) {
    return (1);
  } else {
    return (Number(num) * factorial(Number(num) - 1));
  }
}

console.log(factorial(args[0]));
