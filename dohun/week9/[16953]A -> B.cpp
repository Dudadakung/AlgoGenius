#include <bits/stdc++.h>
using namespace std;

int a, b, res = 0;
bool getRes = false;
queue<int> q;

void Bfs() {
	while (!q.empty()) {
		int size = q.size();
		res++;
		for (int i = 0; i < size; i++) {
			int now = q.front();
			if (now == b) {
				getRes = true;
				while (!q.empty()) {
					q.pop();
				}
				break;
			}
			q.pop();
			if (now < 1000000000) {
				q.push(now * 2);
			}
			if (now <= 100000000) {
				q.push(now * 10 + 1);
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> a >> b;
	
	q.push(a);
	Bfs();

	getRes ? cout << res : cout << -1;
}