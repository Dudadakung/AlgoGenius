#include <bits/stdc++.h>
using namespace std;
#define MAX 1000000000

int tc, num;
int arr[500], memo[500][500];

int DnC(int left, int right) {
  if (memo[left][right] != MAX) {
    return memo[left][right];
  }
  int sum = 0;
  for (int i = left; i < right + 1; i++) {
    sum += arr[i];
  }
  for (int i = left; i < right; i++) {
    memo[left][right] = min(memo[left][right], DnC(left, i) + DnC(i + 1, right) + sum);
  }
  return memo[left][right];
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  
  cin >> tc;
  for (int i = 0; i < tc; i++) {
    fill(memo[0], memo[0] + 500 * 500, MAX);
    cin >> num;
    int sum = 0;
    for (int j = 0; j < num; j++) {
      cin >> arr[j];
      memo[j][j] = arr[j];
      sum += arr[j];
    }
    cout << DnC(0, num - 1) - sum << '\n';
  }
}
