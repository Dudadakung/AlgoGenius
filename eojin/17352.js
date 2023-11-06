const fs = require('fs');
// const input = fs.readFileSync('text.txt').toString().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = Number(input[0]);
const parent = new Array(n + 1).fill(0).map((item, idx) => item = idx);
// console.log(parent);

const findRoot = (x) => {
  if (parent[x] === x) return x;

  return parent[x] = findRoot(parent[x]);
}

const checkRoot = (a, b) => {
  if (findRoot(a) === findRoot(b)) return true;
  return false; 
}

const unionRoot = (a, b) => {
  if (findRoot(a) < findRoot(b)) {
    parent[findRoot(b)] = findRoot(a);
  } else {
    parent[findRoot(a)] = findRoot(b);
  }
}

for(let i = 1; i < n - 1; i++) {
  const [a, b] = input[i].split(' ').map(Number);
  unionRoot(a, b);
}

for (let i = 2; i <= n; i++) {
  if(!checkRoot(1, i)) {
    return console.log(1, i);
  }
}