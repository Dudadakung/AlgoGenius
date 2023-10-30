const fs = require('fs');
const input = fs.readFileSync('text.txt').toString().split('\n');
// const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const size = Number(input[0]);

// 이분 탐색
const binarySearch = (list, target, left, right, mid) => {
  mid = Math.floor((left + right) / 2);

  if (right < left) {
    return list[mid] == target ? 1 : 0;
  }

  if (list[mid] > target) {
    right = mid - 1;
  } else {
    left = mid + 1;
  }

  return binarySearch(list, target, left, right, mid);
}

for(let i = 0; i < size; i++) {
  const N = input[i * 4 + 1];
  const A = input[i * 4 + 2].split(" ").map(v => Number(v));
  const M = input[i * 4 + 3];
  const B = input[i * 4 + 4].split(" ").map(v => Number(v));

  A.sort((a, b) => a - b);

  const result = B.map(v => binarySearch(A, v, 0, A.length - 1, 0));
  console.log(result.join("\n"));
}
  