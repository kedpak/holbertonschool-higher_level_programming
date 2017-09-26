#!/usr/bin/node
// Write a script that display the status code of a GET request.

const request = require('request');
let args = process.argv.slice(2);

request(args[0], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  console.log('code: ' + res.statusCode);
});
