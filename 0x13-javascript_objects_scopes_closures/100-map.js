#!/usr/bin/node
// script that imports an array and computes a new array
// new list multiplies element in accordance to index
const list = require('./100-data').list;
let newList = [];
list.map(function (x, index) {
  newList.push(x * index);

  if (index === list.length - 1) {
    console.log(list);
    console.log(newList);
  }
});
