#include <iostream>
#include <algorithm>
using namespace std;

int N, Map[100][100];

void ipt() {
	cin.sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> N;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			cin >> Map[i][j];
}

void fw() {
	for (int k = 0; k < N; k++)
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				Map[i][j] = max((bool)Map[i][j], Map[i][k] && Map[k][j]);

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++)
			cout << Map[i][j] << ' ';
		cout << '\n';
	}
}

int main() {
	ipt();
	fw();
}