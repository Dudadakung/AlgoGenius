#include <bits/stdc++.h>
using namespace std;
#define MAX 1000000000

int n, k, coin[100], res[100001];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  fill(res, res + 10001, MAX);
  cin >> n >> k;

  for (int i = 0; i < n; i++) {
    cin >> coin[i];
    res[coin[i]] = 1;
  }

  for (int i = 1; i <= k; i++) {
    for (int j = 0; j < n; j++) {
      if (i - coin[j] > 0) {
        res[i] = min(res[i], res[i - coin[j]] + 1);
      }
    }
  }

  if (res[k] == MAX) {
    cout << -1 << '\n';
  } else {
    cout << res[k] << '\n';
  };
}