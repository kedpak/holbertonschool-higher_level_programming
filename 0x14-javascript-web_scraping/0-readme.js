#!/usr/bin/node
/* Write a script that reads and prints the content of a file */

var fs = require('fs');
let args = process.argv.slice(2);

fs.readFile(args[0], 'utf8', function (err, data) {
  if (err) {
    throw err;
  }
  console.log(data);
});
