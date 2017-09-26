#!/usr/bin/node
// Write a class Square that defines a square
// and inherits from Rectangle.

const SquareInher = require('./5-square').Square;

function Square (size) {
  SquareInher.call(this, size);
}

Square.prototype.charPrint = function (c = 'X') {
  let list = [];
  for (let i = 0; i < this.width; i++) {
    for (let j = 0; j < this.height; j++) {
      list.push(c);
    }
    let xPrint = list.join('');
    console.log(xPrint);
    list = [];
  }
};

exports.Square = Square;
