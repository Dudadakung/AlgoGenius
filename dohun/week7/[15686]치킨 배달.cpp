#include <bits/stdc++.h>
using namespace std;

int n, m, arr[50][50], res = 1000000000;
vector<pair<int, int>> chickenLoc;

int getDistance(int sy, int sx, int dy, int dx) {
  return abs(dy - sy) + abs(dx - sx);
}

int getMinDistance(int y, int x) {
  int cost = 1000000000;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (arr[i][j] == 2) {
        cost = min(cost, getDistance(y, x, i, j));
      }
    }
  }
  return cost;
}

void solve(int chickenCount, int prevIndex) {
  if (chickenCount < m) {

    for (int i = prevIndex + 1; i <= chickenLoc.size() - (m - chickenCount); i++) {
      int cy = chickenLoc[i].first;
      int cx = chickenLoc[i].second;
      if (arr[cy][cx] == 2) {
        continue;
      } else {

        arr[cy][cx] = 2;
        solve(chickenCount + 1, i);
        arr[cy][cx] = 0;
      }
    }

  } else {
    int cost = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (arr[i][j] == 1) {
          cost += getMinDistance(i, j);
        }
      }
    }
    res = min(res, cost);
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  
  cin >> n >> m;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> arr[i][j];
      if (arr[i][j] == 2) {
        chickenLoc.push_back({ i, j });
        arr[i][j] = 0;
      }
    }
  }

  solve(0, -1);

  cout << res << '\n';

}