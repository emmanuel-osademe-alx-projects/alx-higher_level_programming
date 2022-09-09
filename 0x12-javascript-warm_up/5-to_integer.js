#!/usr/bin/node
console.log(`${process.argv[2] === undefined ? 'Not a number' : 'My number: ' + parseInt(process.argv[2])}`);
