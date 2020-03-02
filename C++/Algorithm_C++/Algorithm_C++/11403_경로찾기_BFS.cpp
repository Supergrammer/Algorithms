#include <iostream>
#include <queue>
using namespace std;

int N, Map[100][100];
queue<int> Q;

void ipt() {
	cin.sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> N;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			cin >> Map[i][j];
}

void bfs(int n) {
	bool V[100] = { 0 };
	Q.push(n);
	
	while (!Q.empty()) {
		int tmp = Q.front();
		Q.pop();

		for (int i = 0; i < N; i++)
			if (Map[tmp][i] && !V[i]) {
				Q.push(i);
				V[i] = 1;
			}
	}

	for (int i = 0; i < N; i++)
		cout << V[i] << ' ';
	cout << '\n';
}

int main() {
	ipt();
	for (int i = 0; i < N; i++)
		bfs(i);
}