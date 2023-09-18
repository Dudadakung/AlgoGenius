let visited = [];
let curr = 0;

const dfs = (e, r) => {
  visited[r] = ++curr;

  e.get(r).forEach(x => {
    if(visited[x] < 1) {
      dfs(e,x);
    }
  });
}

const findDepth = (input) => {
  const info = input[0].split(' ');
  const nodeNum = Number(info[0]);
  const edgeNum = Number(info[1]);
  const startNode = Number(info[2]);

  curr = 0;
  visited = Array(nodeNum + 1).fill(0);

  const edges = new Map();
  for(let i = 0; i < edgeNum; i++) {
    const edge = input[i + 1].split(' ');
    const key = Number(edge[0]);
    const value = Number(edge[1]);
    
    const keyArray = edges.get(key) || [];
    const valueArray = edges.get(value) || [];
    keyArray.push(value);
    valueArray.push(key);

    edges.set(key, keyArray);
    edges.set(value, valueArray);
  }
  for(item of edges.keys()) {
    const values = edges.get(item).sort((a, b) => a - b);
    edges.set(item, values);
  }

  if (edges.has(startNode)) {
    dfs(edges, startNode);
  } else {
    visited[startNode] = 1;
  }
  
  visited.shift();
  console.log(visited.join('\n'));
}

const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
// let input = fs.readFileSync('text.txt').toString().split('\n');
findDepth(input);