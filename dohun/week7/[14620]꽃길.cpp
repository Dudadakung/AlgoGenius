#include <bits/stdc++.h>
using namespace std;

int n, arr[10][10], res = 1000000000, cnt = 0;
int isVisited[10][10];
int dy[5] = { 0, -1, 0, 1, 0 };
int dx[5] = { 0, 0, -1, 0, 1 };

int getCost() {
  int cost = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (isVisited[i][j]) {
        cost += arr[i][j];
      }
    }
  }
  return cost;
}

bool isInside(int row, int col) {
  return (row >= 0 && col >= 0 && row < n && col < n);
}

void Dfs(int y, int x, int depth) {

  if (depth > 3) {
    res = min(res, getCost());
    return;
  }

  bool isValid = true;
  for (int i = 0; i < 5; i++) {
    int ny = y + dy[i];
    int nx = x + dx[i];
    if (isInside(ny, nx)) {
      isVisited[ny][nx] += 1;
    }
    if (isVisited[ny][nx] > 1) {
      isValid = false;
    }
  }

  if (isValid) {
    for (int i = y; i < n - 1; i++) {
      for (int j = 1; j < n - 1; j++) {
        if (i == y && j <= x - 1)
          continue;
        Dfs(i, j, depth + 1);
      }
    }
  }

  for (int i = 0; i < 5; i++) {
    int ny = y + dy[i];
    int nx = x + dx[i];
    if (isInside(ny, nx)) {
      isVisited[ny][nx] -= 1;
    }
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  
  cin >> n;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> arr[i][j];
    }
  }

  for (int i = 1; i < n - 1; i++) {
    for (int j = 1; j < n - 1; j++) {
      Dfs(i, j, 1);
    }
  }

  cout << res << '\n';
}