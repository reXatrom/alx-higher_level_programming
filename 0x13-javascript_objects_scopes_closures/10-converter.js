#!/usr/bin/node

exports.converter = function (base) {
  return function (fig) {
    return fig.toString(base);
  };
};
