#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counts = 0;
  for (let a = 0; a < list.length; a++) {
    if (searchElement === list[a]) {
      counts++;
    }
  }
  return counts;
};

