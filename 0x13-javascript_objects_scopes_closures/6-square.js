#!/usr/bin/node

const Square_ = require('./5-square');

const Square = class Square extends Square_ {
  charPrint (c) {
    if (c) {
      let result = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.height; j++) {
          result += c;
        }
        console.log(result);
        result = '';
      }
    } else {
      super.print();
    }
  }
};

module.exports = Square;
