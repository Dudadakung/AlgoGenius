const distopia = (input) => {
  const n = Number(input[0]);
  let num = 666;
  let cnt = 1;
  while (cnt < n) {
    num++;
    if(num.toString().includes('666')) cnt++;
  }
  
  console.log(num);
}

const fs = require('fs');
// let input = fs.readFileSync('text.txt').toSring().split('\n');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
distopia(input);
