#!/usr/bin/node
// Function that returns the reserved version of a list

exports.esrever = function (list) {
  let revList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    revList.push(list[i]);
  }
  return revList;
};
