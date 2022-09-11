#!/usr/bin/node
const arg = process.argv;
function factorial (num) {
  if (isNaN(num) || num <= 0) {
    return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(arg[2]));
