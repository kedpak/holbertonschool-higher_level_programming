#!/usr/bin/node
// Write a script that prints the number of movies
// where the character "Wedge Antilles" is present.

let args = process.argv.slice(2);
const request = require('request');

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
  let json = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < json.results.length; i++) {
    for (let j = 0; j < json.results[i].characters.length; j++) {
      if (json.results[i].characters[j] == "https://swapi.co/api/people/18/") {
         count += 1;
	}
     }
  }
  console.log(count);
});
