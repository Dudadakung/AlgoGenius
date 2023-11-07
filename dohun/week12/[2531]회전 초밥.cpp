#include <bits/stdc++.h>
using namespace std;

int n, d, k, c, sushi[30001], numOfSushi[30001], l = 0, r = 0, res = 0, maxRes = 0;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	cin >> n >> d >> k >> c;
	r = k - 1;
	numOfSushi[c]++;
	res++;

	for (int i = 0; i < n; i++) {
		cin >> sushi[i];
		if (r >= i) {
			if (++numOfSushi[sushi[i]] == 1) {
				maxRes = ++res;
			}
		}
	}

	while (l < n - 1) {
		if (++numOfSushi[sushi[++r % n]] == 1) {
			res++;
		}
		if (--numOfSushi[sushi[l++]] == 0) {
			res--;
		}
		maxRes = max(res, maxRes);
	}

	cout << maxRes << '\n';
}