#!/usr/bin/node
const argum = process.argv[2];
if (isNaN(argum)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argum; i++) {
    console.log('#'.repeat(argum));
  }
}
