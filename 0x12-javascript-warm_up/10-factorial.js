#!/usr/bin/node
const factor = function (number) {
  let result = 1;
  let count;
  for (count = number; count > 1; count--) {
    result *= count;
  }
  return result;
};
console.log(factor(process.argv[2]));
