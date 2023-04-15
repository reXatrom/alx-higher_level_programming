#!/usr/bin/node

const num = process.argv[2];

if (!isNaN(parseInt(process.argv[2]))) {
  for (let a = 0; a < num; a++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
