#!/usr/bin/node
// Class defines a Rectangle
// Takes width and height arguments
// If w or h is empty, return empty object

exports.Rectangle = function Rectangle (w, h) {
  if (w == null || w <= 0 || h == null || h <= 0) {
    return;
  }
  this.width = w;
  this.height = h;
  this.print = function () {
    let list = [];
    for (let i = 0; i < h; i++) {
      for (let j = 0; j < w; j++) {
        list.push('X');
      }
      let xPrint = list.join('');
      console.log(xPrint);
      list = [];
    }
  };
  this.rotate = function () {
    let temp = w;
    w = h;
    h = temp;
  };
  this.double = function () {
    h *= 2;
    w *= 2;
  };
};
