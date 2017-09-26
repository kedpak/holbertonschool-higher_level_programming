#!/usr/bin/node
// Function that converts a number from base 10
// to another base passed as argument

exports.converter = function (base) {
  return function (num) {
    return parseInt(num, 10).toString(base);
  };
};
