#!/usr/bin/node

let args = process.argv.slice(2);

let total = 1;
function factorial (num) {
  if (Number(num) === 1 || Number(num) === true) {
    console.log(total);
  } else {
    total *= num;
    return (Number(num) * factorial(Number(num) - 1));
  }
}

factorial(Number(args[0]));
