const fs = require('fs');
const input = fs.readFileSync('dev/stdin').toString().split(' ');

console.log(parseFloat(input[0]) / parseFloat(input[1]));