#include <bits/stdc++.h>
using namespace std;

int n, board[21][21], res = 0, tmp, canCombine;
vector<int> v;

void moveBlocksRight() {
  for (int i = 0; i < n; i++) {
    tmp = 0;
    canCombine = 0;
    for (int j = 0; j < n; j++) {
      if (board[i][n - 1 - j] != 0) {
        v.push_back(board[i][n - 1 - j]);
        ++canCombine;
      } else {
        tmp = 0;
      }
      if (canCombine >= 2 && v.back() == tmp) {
        v.pop_back();
        v.back() *= 2;
        canCombine = 0;
      } else {
        if (!v.empty()) {
          tmp = v.back();
        } else {
          tmp = 0;
        }
      }
    }
    while (v.size() != n) {
      v.push_back(0);
    }
    while(!v.empty()) {
      board[i][n - v.size()] = v.back();
      v.pop_back();
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      res = max(res, board[i][j]);
    }
  }
}

void moveBlocksLeft() {
  for (int i = 0; i < n; i++) {
    tmp = 0;
    canCombine = 0;
    for (int j = 0; j < n; j++) {
      if (board[i][j] != 0) {
        v.push_back(board[i][j]);
        ++canCombine;
      } else {
        tmp = 0;
      }
      if (canCombine >= 2 && v.back() == tmp) {
        v.pop_back();
        v.back() *= 2;
        canCombine = 0;
      } else {
        if (!v.empty()) {
          tmp = v.back();
        } else {
          tmp = 0;
        }
      }
    }
    while (v.size() != n) {
      v.push_back(0);
    }
    while(!v.empty()) {
      board[i][v.size() - 1] = v.back();
      v.pop_back();
    }
  }
  
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      res = max(res, board[i][j]);
    }
  }
}

void moveBlocksUp() {
  for (int i = 0; i < n; i++) {
    tmp = 0;
    canCombine = 0;
    for (int j = 0; j < n; j++) {
      if (board[j][i] != 0) {
        v.push_back(board[j][i]);
        ++canCombine;
      } else {
        tmp = 0;
      }
      if (canCombine >= 2 && v.back() == tmp) {
        v.pop_back();
        v.back() *= 2;
        canCombine = 0;
      } else {
        if (!v.empty()) {
          tmp = v.back();
        } else {
          tmp = 0;
        }
      }
    }
    while (v.size() != n) {
      v.push_back(0);
    }
    while(!v.empty()) {
      board[v.size() - 1][i] = v.back();
      v.pop_back();
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      res = max(res, board[i][j]);
    }
  }
}

void moveBlocksDown() {
  for (int i = 0; i < n; i++) {
    tmp = 0;
    canCombine = 0;
    for (int j = 0; j < n; j++) {
      if (board[n - 1 - j][i] != 0) {
        v.push_back(board[n - 1 - j][i]);
        ++canCombine;
      } else {
        tmp = 0;
      }
      if (canCombine >= 2 && v.back() == tmp) {
        v.pop_back();
        v.back() *= 2;
        canCombine = 0;
      } else {
        if (!v.empty()) {
          tmp = v.back();
        } else {
          tmp = 0;
        }
      }
    }
    while (v.size() != n) {
      v.push_back(0);
    }
    while(!v.empty()) {
      board[n - v.size()][i] = v.back();
      v.pop_back();
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      res = max(res, board[i][j]);
    }
  }
}

void Bt(int depth) {
  if (depth == 5) {
    return;
  }

  int tmpBoard[21][21];
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      tmpBoard[i][j] = board[i][j];
    }
  }

  moveBlocksRight();
  Bt(depth + 1);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      board[i][j] = tmpBoard[i][j];
    }
  }

  moveBlocksLeft();
  Bt(depth + 1);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      board[i][j] = tmpBoard[i][j];
    }
  }

  moveBlocksUp();
  Bt(depth + 1);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      board[i][j] = tmpBoard[i][j];
    }
  }

  moveBlocksDown();
  Bt(depth + 1);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      board[i][j] = tmpBoard[i][j];
    }
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  cin >> n;
  
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> board[i][j];
    }
  }

  Bt(0);

  cout << res << '\n';
}