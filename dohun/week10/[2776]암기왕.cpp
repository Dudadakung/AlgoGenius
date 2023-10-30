#include <bits/stdc++.h>
using namespace std;

int tc, n, m, note[2][1000000];

bool BinarySearch(int value, int l, int r) {
	if (r == l) {
		return (value == note[0][r]) ? true : false;
	}
	int mid = (l + r) / 2;
	if (note[0][l] <= value && value <= note[0][mid]) {
		return BinarySearch(value, l, mid);
	} else if (note[0][mid] < value && value <= note[0][r]) {
		return BinarySearch(value, mid + 1, r);
	}
	return false;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	fill(note[0], note[0] + 1000000, 0);
	fill(note[1], note[1] + 1000000, 0);
	
	cin >> tc;

	for (int i = 0; i < tc; i++) {
		cin >> n;
		for (int j = 0; j < n; j++) {
			cin >> note[0][j];
		}
		cin >> m;
		for (int j = 0; j < m; j++) {
			cin >> note[1][j];
		}

		sort(note[0], note[0] + n);

		for (int j = 0; j < m; j++) {
			cout << BinarySearch(note[1][j], 0, n - 1) << ' ';
		}
	}
}