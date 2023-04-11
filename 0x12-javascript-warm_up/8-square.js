#!/usr/bin/node
let num = process.argv[2];

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let a = 0; a < num; a++) {
    let sqr = '';
    for (let b = 0; b < num; b++) {
      sqr = sqr + 'X';
    }
    console.log(sqr);
  }
}
