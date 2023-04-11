#!/usr/bin/node
exports.addMeMaybe = function (num, theFunction) {
	num = num + 1;
  theFunction(num);
};
