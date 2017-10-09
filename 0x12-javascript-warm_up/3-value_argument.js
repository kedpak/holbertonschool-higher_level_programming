#!/usr/bin/node
// Write a script that prints the first argument passed to it
// If no arguments are passed to the script, print “No argument”
let args = process.argv.slice(2);
if (args[0] != null) {
  console.log(args[0]);
} else {
  console.log('No argument');
}
