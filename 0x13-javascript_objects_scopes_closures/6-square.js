#!/usr/bin/node
// Write a class Square that defines a square
// and inherits from Rectangle.

const Rectangle = require('./4-rectangle').Rectangle;

function Square (size) {
  Rectangle.call(this, size, size);
}

Square.prototype.charPrint = function (c) {
  if (c == null) {
    let rec = new Rectangle(this.width, this.height);
    rec.print();
  } else {
    let list = [];
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.height; j++) {
        list.push(c);
      }
      let xPrint = list.join('');
      console.log(xPrint);
      list = [];
    }
  }
};

exports.Square = Square;
