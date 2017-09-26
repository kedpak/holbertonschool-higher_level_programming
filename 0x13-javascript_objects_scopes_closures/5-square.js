#!/usr/bin/node
// Write a class Square that defines a square
// and inherits from Rectangle.

const Rectangle = require('./4-rectangle').Rectangle;

exports.Square = function Square (size) {
  Rectangle.call(this, size, size);
  this.size = size;
};
