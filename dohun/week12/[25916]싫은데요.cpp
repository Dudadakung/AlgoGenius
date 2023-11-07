#include <bits/stdc++.h>
using namespace std;

int n, m, hole[500000], volume = 0, maxVol = 0, l = 0, r = 0;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> hole[i];
	}

	while (l < n) {
		while (r < n && volume + hole[r] <= m) {
			volume += hole[r];
			r++;
		}
		maxVol = max(maxVol, volume);
		volume -= hole[l];
		l++;
	}

	cout << maxVol << '\n';
}