#include <bits/stdc++.h>
using namespace std;

int n, parent[300001], land1, land2;

int getParent(int num) {
	if (parent[num] == num) {
		return num;
	}
	return parent[num] = getParent(parent[num]);
}

void UnionFind(int a, int b) {
	a = getParent(a);
	b = getParent(b);
	if (a < b) {
		parent[b] = a;
	} else {
		parent[a] = b;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> n;

	for (int i = 1; i <= n; i++) {
		parent[i] = i;
	}

	for (int i = 0; i < n - 2; i++) {
		cin >> land1 >> land2;
		UnionFind(land1, land2);
	}

	int start = getParent(1);
	for (int i = 2; i <= n; i++) {
		if (start != getParent(i)) {
			cout << 1 << ' ' << i << '\n';
			break;
		}
	}
}