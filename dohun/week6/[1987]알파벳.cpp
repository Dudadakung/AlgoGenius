#include <bits/stdc++.h>
using namespace std;

int r, c, res = 0, cnt = 1;
char board[21][21];
bool isVisited[26];
int dy[4] = { -1, 0, 1, 0 };
int dx[4] = { 0, -1, 0, 1 };

bool isInside(int row, int col) {
  return (row >= 1 && col >= 1 && row <= r && col <= c);
}

void Dfs(int y, int x) {

  res = max(res, cnt);
  for (int i = 0; i < 4; i++) {
    int ny = y + dy[i];
    int nx = x + dx[i];
    if (!isVisited[board[ny][nx] - 65] && isInside(ny, nx)) {
      cnt++;
      isVisited[board[ny][nx] - 65] = true;
      Dfs(ny, nx);
      cnt--;
      isVisited[board[ny][nx] - 65] = false;
    }
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  
  cin >> r >> c;
  for (int i = 1; i <= r; i++) {
    for (int j = 1; j <= c; j++) {
      cin >> board[i][j];
    }
  }
  
  isVisited[board[1][1] - 65] = true;
  Dfs(1, 1);

  cout << res << '\n';
}