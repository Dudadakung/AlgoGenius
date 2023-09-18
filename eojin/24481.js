let visited = [];
let depth = [];

const dfs = (e, r, parentDepth) => {
  visited[r] = true;
  depth[r] = parentDepth + 1;

  e.get(r).forEach(x => {
    if(!visited[x]) {
      dfs(e,x, depth[r]);
    }
  });
}

const findDepth = (input) => {
  const info = input[0].split(' ');
  const nodeNum = Number(info[0]);
  const edgeNum = Number(info[1]);
  const startNode = Number(info[2]);

  visited = Array(nodeNum + 1).fill(false);
  depth = Array(nodeNum + 1).fill(-1);

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
    dfs(edges, startNode, -1);
  } else {
    visited[startNode] = true;
    depth[startNode] = 0;
  }
  
  const result = depth.slice(1);
  console.log(result.join('\n'));
}

const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
// let input = fs.readFileSync('text.txt').toString().split('\n');
findDepth(input);