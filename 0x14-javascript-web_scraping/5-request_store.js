#!/usr/bin/node
// Write a script that gets the contents of
// a webpage and stores it in a file.

let args = process.argv.slice(2);
const request = require('request');
let fs = require('fs');

const options = {
  url: args[0],
  method: 'GET',
  headers: {
    'Accept': 'text/html',
    'Accept-Charset': 'utf-8',
    'User-Agent': 'kpak'
  }
};

request(options, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(args[1], body, 'utf-8', function (err, data) {
    if (err) {
      return console.log(err);
    }
  });
});
