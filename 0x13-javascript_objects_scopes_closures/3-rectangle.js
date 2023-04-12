#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      let sqr = '';
      for (let b = 0; b < this.width; b++) {
        sqr += 'X';
      }
      console.log(sqr);
    }
  }
}

module.exports = Rectangle;
