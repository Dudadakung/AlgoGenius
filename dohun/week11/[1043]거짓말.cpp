#include <bits/stdc++.h>
using namespace std;

int n, m, knowNum, know[51], partyNum[51], party[51][51], num;
int minParent = 1000000, res;

int getParent(int num) {
	if (know[num] == num) {
		return num;
	}
	return know[num] = getParent(know[num]);
}

void UnionFind(int a, int b) {
	a = getParent(a);
	b = getParent(b);
	if (a < b) {
		know[b] = a;
	} else {
		know[a] = b;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	for (int i = 1; i <= 51; i++) {
		know[i] = i;
	}

	cin >> n >> m;

	cin >> knowNum;
	for (int i = 1; i <= knowNum; i++) {
		cin >> num;
		know[num] = 0;
	}
	for (int i = 1; i <= m; i++) {
		cin >> partyNum[i];
		for (int j = 1; j <= partyNum[i]; j++) {
			cin >> party[i][j];
		}
		for (int j = 1; j <= partyNum[i]; j++) {
			for (int k = j + 1; k <= partyNum[i]; k++) {
				UnionFind(party[i][j], party[i][k]);
			}
		}
	}

	for (int i = 1; i <= m; i++) {
		for (int j = 1; j <= partyNum[i]; j++) {
			for (int k = j + 1; k <= partyNum[i]; k++) {
				UnionFind(party[i][j], party[i][k]);
			}
		}
	}

	res = m;

	for (int i = 1; i <= m; i++) {
		for (int j = 1; j <= partyNum[m]; j++) {
			if (know[party[i][j]] == 0) {
				res--;
			}
			break;
		}
	}

	cout << res << '\n';
}