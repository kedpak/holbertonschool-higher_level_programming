#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie

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
  let charList = [];
  /* first loop grabs character ID from character list */
  for (let j = 0; j < json.characters.length; j++) {
    let charStr = json.characters[j].slice(28, 30);
    charStr = parseInt(charStr, 10);
    charList.push(charStr);
  }
  /* second loop grabs character name through new request and prints */
  for (let j = 0; j < charList.length; j++) {
    let options2 = {
      url: 'http://swapi.co/api/people/' + charList[j],
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Accept-Charset': 'utf-8',
        'User-Agent': 'kpak'
      }
    };
    request(options2, function (err, res, body) {
      if (err) {
        console.log(err);
      }
      let json2 = JSON.parse(body);
      console.log(json2.name);
    });
  }
});
