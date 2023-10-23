const atob = (input) => {
  const a = Number(input[0]);
  const b = Number(input[1]);
  
  const queue = [a, 1]; // 현재 값과 count

  while (queue.length) {
    const now = queue.shift();
    const cnt = queue.shift();

    if (now === b) {
      return cnt;
    }
    else {
      if (now * 2 <= b) {
        queue.push(now * 2, cnt + 1);
      }
      if (Number(now + '1') <= b) {
        queue.push(Number(now + '1'), cnt + 1);
      }
    }
  }

  return -1;
}

const fs = require('fs');
let input = fs.readFileSync('text.txt').toString().split(' ');
// let input = fs.readFileSync('/dev/stdin').toString().split(' ');
console.log(atob(input));