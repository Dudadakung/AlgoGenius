#include <bits/stdc++.h>
using namespace std;

int n, m, r, u, v;
int visited[100001];
vector<int> vertex[100001];

void Dfs(int nextV) {
  for (int i = 0; i < vertex[nextV].size(); i++) {
    if(visited[vertex[nextV][i]] == -1) {
      visited[vertex[nextV][i]] = visited[nextV] + 1;
      Dfs(vertex[nextV][i]);
    }
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  fill(visited, visited + 100001, -1);
  
  cin >> n >> m >> r;
  visited[r] = 0;

  for (int i = 0; i < m; i++) {
    cin >> u >> v;
    vertex[u].push_back(v);
    vertex[v].push_back(u);
  }

  for (int i = 1; i <= n; i++) {
    sort(vertex[i].begin(), vertex[i].end());
  }

  Dfs(r);

  for (int i = 1; i <= n; i++) {
    cout << visited[i] << '\n';
  }
}