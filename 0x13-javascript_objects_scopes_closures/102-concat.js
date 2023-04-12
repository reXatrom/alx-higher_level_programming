#!/usr/bin/node

const fs = require('fs');

const firstfileArg = fs.readFileSync(process.argv[2]).toString();
const secondfileArg = fs.readFileSync(process.argv[3]).toString();

fs.writeFileSync(process.argv[4], firstfileArg + secondfileArg);
