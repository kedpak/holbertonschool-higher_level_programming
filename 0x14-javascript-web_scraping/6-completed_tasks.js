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
  let count = 0;
  let bodyData = JSON.parse(body);
  for (let i = 0; i < bodyData.length; i++) {
    if (i > 0 && bodyData[i - 1].userId !== bodyData[i].userId) {
      dict[bodyData[i - 1].userId] = count;
      count = 0;
    } else if (i + 1 === bodyData.length) {
      dict[bodyData[i].userId] = count;
    }
    if (bodyData[i].completed === true) {
      count += 1;
    }
  }
  console.log(dict);
});
