const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


rl.on('line', (line) => {
    const input = line.split(' ');
    const a = parseInt(input[0], 10);
    const b = parseInt(input[1], 10);

    console.log('a = ' + a);
    console.log('b = ' + b);
    rl.close();
});
