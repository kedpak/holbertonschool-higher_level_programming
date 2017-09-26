#!/usr/bin/node
// Class defines a Rectangle
// Takes width and height arguments
// If w or h is empty, return empty object

exports.Rectangle = function Rectangle (w, h) {
  if (w === null || w <= 0 || h === null || h <= 0) {
    return;
  }
  this.width = w;
  this.height = h;
};
