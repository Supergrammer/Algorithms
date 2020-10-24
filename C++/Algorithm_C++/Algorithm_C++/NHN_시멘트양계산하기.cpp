#include <iostream>
#include <sstream>

using namespace std;

int build[100];

int cement(int block, int width) {
	int l, r;
	l = r = build[block];

	for (int i = block; i >= 0; i--)
		if (l < build[i]) l = build[i];
	for (int i = block; i < width; i++)
		if (r < build[i]) r = build[i];

	return min(l, r);
}

void solution(int day, int width, int** blocks) {
	// TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
	int answer = 0;

	for (int i = 0; i < day; i++) {
		for (int j = 0; j < width; j++)
			build[j] += blocks[i][j];
 
		for (int j = 1; j < width - 1; j++) {
			int tmp = cement(j, width);
			if (build[j] != tmp) {
				answer += tmp - build[j];
				build[j] = tmp;
			}
		}
	}

	cout << answer;
}

struct input_data {
	int day;
	int width;
	int** blocks;
};

void process_stdin(struct input_data& inputData) {
	string line;
	istringstream iss;

	getline(cin, line);
	iss.str(line);
	iss >> inputData.day;

	getline(cin, line);
	iss.clear();
	iss.str(line);
	iss >> inputData.width;

	inputData.blocks = new int* [inputData.day];
	for (int i = 0; i < inputData.day; i++) {
		getline(cin, line);
		iss.clear();
		iss.str(line);
		inputData.blocks[i] = new int[inputData.width];
		for (int j = 0; j < inputData.width; j++) {
			iss >> inputData.blocks[i][j];
		}
	}
}

int main() {
	struct input_data inputData;
	process_stdin(inputData);

	solution(inputData.day, inputData.width, inputData.blocks);
	return 0;
}