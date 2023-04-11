#!/usr/bin/node

function sec (myArray) {
  if (myArray.length === 2 || myArray.length === 3) {
	return (0);
}

  let max = myArray[2];
  let secMax = myArray[3];

  for (let a = 2; a < myArray.length; a++) {
    if (myArray[a] > max) {
      secMax = max;
      max = myArray[a];
    } else if (myArray[a] > secMax && myArray[a] < max) {
      secMax = myArray[a];
    }
  }
  return (secMax);
}

console.log(sec(process.argv));
