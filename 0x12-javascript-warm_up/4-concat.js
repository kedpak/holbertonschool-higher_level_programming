#!/usr/bin/node
//Write a script that prints two arguments passed 
// to it, in the following format: “ is ”
let args = process.argv.slice(2);

if (args.length === 2) {
  console.log(args[0] + ' is ' + args[1]);
} else if (args.length === 1) {
  console.log(args[0] + ' is undefined');
} else if (args.length <= 0) {
  console.log('undefined is undefined');
}
