const calcPrice = (x, y, board) => {
  let price = 0;
  // [n,n], [n, n+1], [n, n-1], [n-1, n], [n+1, n]
  const dx = [0,0,0,-1,1]; 
  const dy = [0,1,-1,0,0];

  for(let i = 0; i < 5; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];
    price += board[nx][ny]; // 각 블록 가격 합
  }

  return price;
}

const isImPossible = (x, y, z, w) => {
  const column = Math.pow(Math.abs(x-z), 2); // x와 z의 차이의 제곱 = a칸과 b칸의 열 간격
  const row = Math.pow(Math.abs(y-w), 2); // y와 w의 차이의 제곱 = a칸과 b칸의 행 간격
  if (column + row <= 4) { // 열과 행 중 하나라도 2칸 이상 차이가 나면 possible인데, 2칸 이상 차이가 나는 게 없다면 impossible
    return true;
  }
  return false;
}

const flowerRoad = (input) => {
  const size = Number(input[0]); // 화단의 한 변의 길이
  const originPrice = [];
  // 화단의 지점당 가격 저장
  for(let i = 0; i < size; i++) {
    const row = input[i + 1].split(' ').map((item) => Number(item));
    originPrice[i] = row;
  }

  const priceBoard = Array.from(Array(size), () => Array(size).fill(0)); // 2차원 배열 생성

  for(let i = 1; i < size - 1; i++) {
    for (let j = 1; j < size - 1; j++) {
      priceBoard[i][j] = calcPrice(i, j, originPrice); // 맨 끝 라인들 빼고, 각 블록에 꽃을 심었을 때의 비용 저장
    }
  }

  let min = Infinity;
  for (let a = 1; a < size - 1; a++) { // 첫 번째 꽃 행
    for (let b = 1; b < size - 1; b++) { // 첫 번째 꽃 열
      for (let c = 1; c < size - 1; c++) {  // 두 번째 꽃 행
        for (let d = 1; d < size - 1; d++) { // 두 번재 꽃 열
          if (isImPossible(a,b,c,d)) continue; // 첫 번째 꽃 [a,b]과 두 번째 꽃 [c,d] 가 2칸 이상 차이가 나는지 안 나는지
          for (let e = 1; e < size - 1; e++) { // 세 번째 꽃 행
            for (let f = 1; f < size - 1; f++) { // 세 번째 꽃 열 
              if (isImPossible(a,b,e,f)) continue; // 첫 번째 꽃 [a,b]과 세 번째 꽃 [e,f] 가 2칸 이상 차이가 나는지 안 나는지
              if (isImPossible(c,d,e,f)) continue; // 두 번째 꽃 [c,d]과 세 번째 꽃 [e,f] 가 2칸 이상 차이가 나는지 안 나는지
              let temp = priceBoard[a][b] + priceBoard[c][d] + priceBoard[e][f]; // 꽃1 가격 + 꽃2 가격 + 꽃3 가격
              if (temp < min) min = temp; // 최소값이면 저장
            }
          }
        }
      }
    }
  }

  console.log(min);
}


const fs = require('fs');
// let input = fs.readFileSync('text.txt').toString().split('\n');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
flowerRoad(input);