#!/usr/bin/node
// The constructor is used to stablished the object properties or to call the methods to prepare the object for use
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }

  // method that prints a rectangle
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // method that prints a rectangle
  rotate () {
    const a = this.width;
    this.width = this.height;
    this.height = a;
  }

  // method that prints a rectangle
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
