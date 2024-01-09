#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let j = 0; j < this.height; j++) {
      let st = '';
      for (let k = 0; k < this.width; k++) {
        st += c;
      }
      console.log(st);
    }
  }
}
module.exports = Square;
