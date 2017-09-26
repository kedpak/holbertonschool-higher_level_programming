#!/usr/bin/node
// Script that writes a string to a file

let fs = require('fs');
let args = process.argv.slice(2);

fs.writeFile(args[0], args[1], 'utf-8', function (err, data) {
  if (err) {
    return console.log(err);
  }
});
