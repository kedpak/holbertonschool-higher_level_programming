#!/usr/bin/node
// Function that prints the number of argument
// already printed and the new argument value

let funcCount = 0;

exports.logMe = function (item) {
  console.log(funcCount + ': ' + item);
  funcCount += 1;
};
