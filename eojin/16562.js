// const fs = require('fs');
// const input = fs.readFileSync('text.txt').toString().split('\n');
// // const input = fs.readFileSync('/dev/stdin').toString().split('\n');

// const [N, M, K] = input[0].split(' ').map(Number);
// const needed = [0, ...input[1].split(' ').map(Number)];
// const parent = new Array(N + 1).fill(0).map((item, idx) => item = idx);
// // console.log(needed);
// // console.log(parent);

// const getParent = (x) => {
//   if (parent[x] === x) return x;

//   return parent[x] = getParent(parent[x]);
// }

// const unionParent = (a, b) => {
//   if (getParent(a) <= getParent(b)) {
//     parent[getParent(b)] = getParent(a);
//   } else {
//     parent[getParent(a)] = getParent(b);
//   }
// }

// for (let i = 0; i < M; i++) {
//   const [a, b] = input[i + 2].split(' ').map(Number);
//   unionParent(a, b);
// }

// const group = new Map();
// for(let i = 1; i < N + 1; i++) {
//   const nowParent = getParent(i);
//   if(group.has(nowParent)) {
//     const nowValue = group.get(nowParent);
//     if(Array.isArray(nowValue)) {
//       nowValue.push(i);
//       group.set(nowParent, nowValue)
//     } else {
//       group.set(nowParent, [nowValue, i]);
//     }
//   } else {
//     group.set(nowParent, i);
//   }
// }

// const findMinMoney = (values) => {
//   let min = Infinity;

//   if (Array.isArray(values)) {
//     values.forEach(i => {
//       if (needed[i] < min) {
//         min = needed[i];
//       }
//     });
//   } else {
//     min = values;
//   }

//   return min;
// }

// let totalMoney = 0;

// const keys = group.keys();
// for(let key of keys) {
//   const values = group.get(key);
//   totalMoney += findMinMoney(values);
// }

// console.log(totalMoney > K ? 'Oh no' : totalMoney);

const [[N, M, K], cost, ...input] = require("fs")
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => {
    v = v.split(" ").map(Number);
    return v;
  });

let answer = 0;
cost.unshift(0);
const costCheck = [];

const set = Array.from({ length: N + 1 }, (v, i) => i);
const check = Array.from({ length: N + 1 }, () => false);

function find(parent) {
  if (set[parent] === parent) return parent;
  return (set[parent] = find(set[parent]));
}

function union(a, b) {
  const parentA = find(a);
  const parentB = find(b);

  if (cost[parentA] > cost[parentB]) {
    set[parentA] = parentB;
    check[parentA] = true;

    if (!check[parentB]) {
      //   answer += cost[parentB];
      check[parentB] = true;
    }
    // find(set[parentA]);
  } else {
    set[parentB] = parentA;
    check[parentB] = true;

    if (!check[parentA]) {
      //   answer += cost[parentA];
      check[parentA] = true;
    }
    // find(set[parentB]);
  }
}

input.forEach((v) => {
  const [a, b] = v;
  union(a, b);
});

for (let i = 1; i < set.length; i++) {
  find(i);
  if (costCheck.indexOf(set[i]) === -1) {
    answer += cost[set[i]];
    costCheck.push(set[i]);
  }
}
// console.log(set);
// console.log(answer);
answer <= K ? console.log(answer) : console.log("Oh no");