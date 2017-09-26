#!/usr/bin/node
// Write a class Square that defines a square
// and inherits from Rectangle.

const Rectangle = require('./4-rectangle').Rectangle;

exports.Square = function Square (size) {
  Rectangle.call(this, size, size);

  this.charPrint = function charPrint (c) {
    if (c == null) {
      let rec = new Rectangle(size, size);
      rec.print();
    } else {
      let list = [];
      for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
          list.push(c);
        }
        let xPrint = list.join('');
        console.log(xPrint);
        list = [];
      }
    }
  };
};
