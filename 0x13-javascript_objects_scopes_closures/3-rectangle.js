#!/usr/bin/node
// The constructor is used to stablished the object properties or to call the methods to prepare the object for use
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }

  // Getter
  get printRec () {
    return this.print();
  }

  // method that prints a rectangle
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
