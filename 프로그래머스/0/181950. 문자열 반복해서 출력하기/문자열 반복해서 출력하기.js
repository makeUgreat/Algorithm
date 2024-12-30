require('readline')
    .createInterface({  input : process.stdin, outut : process.stdout})
    .on('line', (line) => {
    const [str,iter] = line.split(' ');
    console.log(str.repeat(+iter));
});
      
    