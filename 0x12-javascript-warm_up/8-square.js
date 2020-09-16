#!/usr/bin/node
const argum = process.argv;
if (argum.length === 2 || isNaN(argum[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argum[2]; i++) {
    console.log('#'.repeat(argum[2]));
  }
}
