const fs = require('fs');

// const input = fs.readFileSync('text.txt').toString().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [N, d, k, c] = input[0].split(' ').map(Number);
const sushiList = [];

for (let i = 0; i < N; i++) {
  sushiList.push(Number(input[i + 1]));
}

let start = 0;
let end = k - 1;
let maxCount = 0;
let currentSushiList = []
const isInclude = new Array(d + 1).fill(false);

const couponFlag = sushiList.includes(c);

const checkCount = (list) => {
  if(list.includes(c)) {
    return isInclude.filter(Boolean).length;
  } else {
    return isInclude.filter(Boolean).length + 1;
  }
}

for (let i = start; i <= end; i++) {
  currentSushiList.push(sushiList[i]);
  isInclude[sushiList[i]] = true;
}

maxCount = checkCount(currentSushiList);

while (maxCount !== k + 1) {
  start++;
  end++;

  if (end >= N) end = 0;

  if (start > end && end >= k - 1) {
    return console.log(maxCount);
  }

  const shiftItem = currentSushiList.shift();
  if (!currentSushiList.includes(shiftItem)) isInclude[shiftItem] = false;
  currentSushiList.push(sushiList[end]);
  isInclude[sushiList[end]] = true;

  // console.log("CURRENT LIST : ", currentSushiList);

  maxCount = Math.max(maxCount, checkCount(currentSushiList));
}

console.log(maxCount);
