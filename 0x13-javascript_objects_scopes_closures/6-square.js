#!/usr/bin/node
// Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js
const square = require('./5-square');
class Square extends square {
  // method that prints a rectangle usign 'C' char
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
