#!/usr/bin/node

const Rectangle = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let result = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        result = result + 'X';
      }
      console.log(result);
      result = '';
    }
  }
};

module.exports = Rectangle;
