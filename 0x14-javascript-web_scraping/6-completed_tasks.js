#!/usr/bin/node
// Write a script that computes the number
// of tasks completed by user id.

const request = require('request');
let args = process.argv.slice(2);

const options = {
  url: args[0],
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Accept-Charset': 'utf-8',
    'User-Agent': 'kpak'
  }
};

request(options, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  let dict = {};
  let bodyData = JSON.parse(body);
  for (let i = 0; i < bodyData.length; i++) {
    if (bodyData[i].completed === true) {
      if (dict.hasOwnProperty(bodyData[i].userId) === false) {
        dict[bodyData[i].userId] = 1;
      } else {
        dict[bodyData[i].userId] += 1;
      }
    }
  }
  console.log(dict);
});
