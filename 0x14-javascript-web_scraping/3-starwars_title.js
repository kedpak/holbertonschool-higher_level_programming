#!/usr/bin/node
// Write a script that prints the title of a Star Wars
// movie where the episode number matches a given integer.

let args = process.argv.slice(2);
const request = require('request');

const options = {
  url: 'http://swapi.co/api/films/' + args[0],
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
  let json = JSON.parse(body);
  console.log(json.title);
});
