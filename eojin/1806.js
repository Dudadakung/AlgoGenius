const fs = require('fs');
// const input = fs.readFileSync('text.txt').toString().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [N, S] = input[0].split(' ').map(Number);
const nums = input[1].split(' ').map(Number);

if (nums[0] >= S) {
  return console.log(1);
}

let start = 0;
let end = 1;
let currentNums = [nums[start], nums[end]];
let currentSum = nums[start] + nums[end];
let minCount = Infinity;

while (end < N) {
  if (currentSum >= S) {
    minCount = Math.min(minCount, currentNums.length);
    currentSum -= currentNums.shift();
    start++;
  }
  
  if (currentSum < S) {
    end++;
    currentNums.push(nums[end]);
    currentSum += nums[end];
  }
}

console.log(minCount === Infinity ? 0 : minCount);