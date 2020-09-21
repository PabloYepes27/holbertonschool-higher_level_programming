#!/usr/bin/node
// The constructor is used to stablished the object properties or to call the methods to prepare the object for use
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }
}
module.exports = Rectangle;
