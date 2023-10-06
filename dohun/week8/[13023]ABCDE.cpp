#include <bits/stdc++.h>
using namespace std;

int n, m, a, b;
vector<int> v[2000];
bool isVisited[2000];

void Dfs(int parent, int depth) {
  if (depth == 4) {
    cout << 1 << '\n';
    exit(0);
  }
  for (int i = 0; i < v[parent].size(); i++) {
    if (!isVisited[v[parent][i]]) {
      isVisited[v[parent][i]] = true;
      Dfs(v[parent][i], depth + 1);
      isVisited[v[parent][i]] = false;
    }
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  
  cin >> n >> m;
  for (int i = 0; i < m; i++) {
    cin >> a >> b;
    v[a].push_back(b);
    v[b].push_back(a);
  }

  for (int i = 0; i < n; i++) {
    isVisited[i] = true;
    Dfs(i, 0);
    isVisited[i] = false;
  }

  cout << 0 << '\n';
}