const sumCost = (input) => {
  const testNum = Number(input[0]);
  for(let i = 0; i < testNum; i++) {
    const chapterSize = Number(input[2 * i + 1]); // 챕터 수

    const chapters = input[2 * i + 2].split(' ').map((item) => Number(item)); // 각 챕터 크기 저장
    chapters.unshift(0);
    const sum = [0];
    const dp = Array.from(Array(chapterSize + 1), () => Array(chapterSize + 1).fill(0));

    for(let k = 1; k <= chapterSize; k++) {
      sum[k] = sum[k-1] + chapters[k];
    }
    // console.log(sum);

    for (let gap = 1; gap < chapterSize; gap++) {
      for (let start = 1; start + gap <= chapterSize; start++) {
        const end = start + gap;
        dp[start][end] = Infinity;
        for(let mid = start; mid < end; mid++) {
          dp[start][end] = Math.min(dp[start][end], dp[start][mid] + dp[mid + 1][end] + sum[end] - sum[start - 1]);
        }
      }
    }

    console.log(dp[1][chapterSize]);
  }
}

const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
// let input = fs.readFileSync('text.txt').toString().split('\n');
// console.log(input)
sumCost(input)