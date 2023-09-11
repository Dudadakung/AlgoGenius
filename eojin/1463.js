const countWay = (input) => {
  const testNum = Number(input[0]);
  for(let i = 0; i < testNum; i++) {
    const n = Number(input[i + 1]);
    const dp = [];
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;

    for(let j = 4; j <= n; j++) {
      dp[j] = dp[j-1] + dp[j-2] + dp[j-3];
    };

    console.log(dp[n]);
  }
}


const fs = require('fs');
// const input = fs.readFileSync('text.txt').toString().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
countWay(input);