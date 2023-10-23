const x = [-2, -2, 0, 0, 2, 2];
const y = [-1, 1, -2, 2, -1, 1];

const deathKnight = (input) => {
  const size = Number(input[0]);
  const [r1, c1, r2, c2] = input[1].split(' ').map(item => Number(item));
  const visited = Array.from(Array(size), () => Array(size).fill(false));

  visited[r1][c1] = true;

  const queue = [[r1, c1, 0]];

  while (queue.length) {
    const [row, col, cnt] = queue.shift();

    if (row === r2 && col === c2) {
      return cnt;
    }
    else {
      for (let i = 0; i < x.length; i++) {
        if (row + x[i] < size && row + x[i] >= 0
          && col + y[i] < size && col + y[i] >= 0
          && !visited[row + x[i]][col + y[i]]) {
            visited[row + x[i]][col + y[i]] = true;
          queue.push([row + x[i], col + y[i], cnt + 1]);
        }
      }
    }
  }
  return -1;
}

const fs = require('fs');
// let input = fs.readFileSync('text.txt').toString().split('\n');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
console.log(deathKnight(input));