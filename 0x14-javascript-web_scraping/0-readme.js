#!/usr/bin/node
/* Write a script that reads and prints the content of a file */

let fs = require('fs');
let args = process.argv.slice(2);

fs.readFile(args[0], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
