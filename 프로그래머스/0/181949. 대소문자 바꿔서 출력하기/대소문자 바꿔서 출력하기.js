require('readline')
    .createInterface({ input: process.stdin, output: process.stdout})
    .on('line', (line) => {
    let res = '';
    for (let char of line) {
        res += transform(char);
    }
    console.log(res);
})

function transform(char) {
    const asci = char.charCodeAt(0);
    if (asci >= 65 && asci <= 90) {
        return char.toLowerCase();
    }
    if (asci >= 97 && asci <= 122) {
        return char.toUpperCase();
    }
    return char;
}