#!/usr/bin/node

let args = process.argv.slice(2);
if (args[0] != null) {
  console.log(args.join(' '));
} else {
  console.log('No Argument');
}
