const findNum = (cur, end, max, cnt) => {
  // console.log("max" + max + "| cnt" + cnt);
  // console.log("cur", cur);
  
  if (max === cnt) {
    return [];
  }
  // console.log('findNum')
  
  const total = [];
  for(let k = 1; k <= end; k++) {
    const row = []
    // console.log("k" + k);
    if (cur.includes(k)) {
      continue;
    } else {
      const under = [...findNum([...cur, k], end, max, cnt + 1)];
      // console.log("under : ", under);
      if (under.length <= 0) {
        row.push(k);
      } else {
        for (let j = 0; j < under.length; j++) {
          // console.log("Under J");
          // console.log(under[j]);
          
          if (Array.isArray(under[j])) {
            // under[j]가 배열인 경우
            row.push([k, ...under[j]]);
          } else {
            // under[j]가 배열이 아닌 경우 (숫자 또는 다른 데이터 유형)
            row.push([k, under[j]]);
          }
        }
      }
    }
    // console.log("row : ", ...row);
    total.push(...row);
  }
  // console.log("ORER : " + cnt + " | TOTAL : ", total);
  return total;
}

const mnm = (input) => {
  const n = Number(input[0]);
  const m = Number(input[1]);
  const nums = [];
  // console.log(n);
  // console.log(m);

  if (m === 1) {
    //하나씩 출력
    for(let i = 1; i <= n; i++) {
      console.log(i);
    }
    return;
  }

  // i로 시작하는 수열 (i보다 전 수는 들어가지 않음)
  for(let i = 1; i <= n; i++) {
    const row = [];
    // m -1 개의 수를 i + 1 ~ n 중 구해야 함
    // 중복은 있으면 안됨
    const under = [...findNum([i], n, m, 1)];
    // console.log("under : ", under);
    for (let j = 0; j < under.length; j++) {
      if (Array.isArray(under[j])) {
        row.push([i, ...under[j]]);
      } else {
        row.push([i, under[j]]);
      }
    }
    nums.push(row);
  }

  // console.log("FINAL");
  for(first of nums) {
    for(second of first) {
      console.log(second.join(" "));
    }
  }
}

const fs = require('fs');
// let input = fs.readFileSync('text.txt').toString().split(' ');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');
mnm(input);

// const mnm = (input) => {
//   const n = Number(input[0]);
//   const m = Number(input[1]);
  
//   const nums = [...Array(m)].fill(0);
//   const visited = [...Array(m)].fill(false);

//   let result = "";

//   const findNums = (cnt) => {
//     if (cnt === m) {
//       const arr = [];
//       for (let i = 0; i < m; i++) {
//         arr.push(nums[i]);
//       }
//       return result += `${arr.join(' ')}\n`;
//     }
//     for (let i = 1; i <= n; i++) {
//       if (!visited[i]) {
//         nums[cnt] = i;
//         visited[i] = true;
//         findNums(cnt + 1);
//         visited[i] = false;
//       }
//     }
//   }

//   findNums(0);

//   console.log(result);
// }

// const fs = require('fs');
// // let input = fs.readFileSync('text.txt').toString().split(' ');
// let input = fs.readFileSync('/dev/stdin').toString().split(' ');
// mnm(input);