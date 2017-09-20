#!/usr/bin/node

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
