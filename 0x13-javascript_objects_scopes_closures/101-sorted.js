#!/usr/bin/node

const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDic = {};

for (const a in valsUniq) {
  const list = [];
  for (const b in totalist) {
    if (totalist[b][1] === valsUniq[a]) {
      list.unshift(totalist[b][0]);
    }
  }
  newDic[valsUniq[a]] = list;
}
console.log(newDic);
