#include <iostream>
#include <sstream>

using namespace std;

int player[25], catchers[26];
bool quickPlayers[26];
int now = 0, catcher = 0;

void solution(int numOfAllPlayers, int numOfQuickPlayers, char* namesOfQuickPlayers, int numOfGames, int* numOfMovesPerGame) {
	// TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
	for (int i = 0; i < numOfAllPlayers - 1; i++)
		player[i] = i + 1;
	for (int i = 0; i < numOfQuickPlayers; i++)
		quickPlayers[namesOfQuickPlayers[i] - 'A'] = true;
	catchers[catcher] += 1;

	for (int i = 0; i < numOfGames; i++) {
		now = (now + numOfMovesPerGame[i]) % (numOfAllPlayers - 1);
		if (now < 0) now += (numOfAllPlayers - 1);
		if (quickPlayers[player[now]]) {
			catchers[catcher] += 1;
			continue;
		}

		int tmp = catcher;
		catcher = player[now];
		player[now] = tmp;
		catchers[catcher] += 1;
	}


	for (int i = 0; i < numOfAllPlayers - 1; i++)
		cout << char(player[i] + 'A') << ' ' << catchers[player[i]] << '\n';
	cout << char(catcher + 'A') << ' ' << catchers[catcher] << '\n';
}

struct input_data {
	int numOfAllPlayers;
	int numOfQuickPlayers;
	char* namesOfQuickPlayers;
	int numOfGames;
	int* numOfMovesPerGame;
};

void process_stdin(struct input_data& inputData) {
	string line;
	istringstream iss;

	getline(cin, line);
	iss.str(line);
	iss >> inputData.numOfAllPlayers;

	getline(cin, line);
	iss.clear();
	iss.str(line);
	iss >> inputData.numOfQuickPlayers;

	getline(cin, line);
	iss.clear();
	iss.str(line);
	inputData.namesOfQuickPlayers = new char[inputData.numOfQuickPlayers];
	for (int i = 0; i < inputData.numOfQuickPlayers; i++) {
		iss >> inputData.namesOfQuickPlayers[i];
	}

	getline(cin, line);
	iss.clear();
	iss.str(line);
	iss >> inputData.numOfGames;

	getline(cin, line);
	iss.clear();
	iss.str(line);
	inputData.numOfMovesPerGame = new int[inputData.numOfGames];
	for (int i = 0; i < inputData.numOfGames; i++) {
		iss >> inputData.numOfMovesPerGame[i];
	}
}

int main() {
	struct input_data inputData;
	process_stdin(inputData);

	solution(inputData.numOfAllPlayers, inputData.numOfQuickPlayers, inputData.namesOfQuickPlayers, inputData.numOfGames, inputData.numOfMovesPerGame);
	return 0;
}