#include <iostream>
#include <sstream>
#include <stack>

using namespace std;

void solution(int numOfOrder, string* orderArr) {
	// TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.

	for (int i = 0; i < numOfOrder; i++) {
		stack<int> num;
		stack<char> RGB, tmp;

		string answer;
		for (int j = 0; j < orderArr[i].size(); j++) {
			if (orderArr[i][j] >= '1' && orderArr[i][j] <= '9')
				num.push(orderArr[i][j] -= '0');
			else if (orderArr[i][j] == ')') {
				while (1) {
					char c = RGB.top();
					RGB.pop();

					if (c == '(') break;
					else tmp.push(c);
				}

				string tmps, rtn;
				
				int n;
				if (num.empty()) n = 1;
				else {
					n = num.top();
					num.pop();
				}

				while (!tmp.empty()) {
					tmps += tmp.top();
					tmp.pop();
				}

				for (int k = 0; k < n; k++)
					rtn += tmps;

				for (int k = 0; k < rtn.size(); k++)
					RGB.push(rtn[k]);
			}
			else RGB.push(orderArr[i][j]);
		}

		while (!RGB.empty()) {
			answer = RGB.top() + answer;
			RGB.pop();
		}
		cout << answer << '\n';
	}
}

struct input_data {
	int numOfOrder;
	string* orderArr;
};

void process_stdin(struct input_data& inputData) {
	string line;
	istringstream iss;

	getline(cin, line);
	iss.str(line);
	iss >> inputData.numOfOrder;

	inputData.orderArr = new string[inputData.numOfOrder];
	for (int i = 0; i < inputData.numOfOrder; i++) {
		getline(cin, line);
		iss.clear();
		iss.str(line);
		iss >> inputData.orderArr[i];
	}
}

int main() {
	struct input_data inputData;
	process_stdin(inputData);

	solution(inputData.numOfOrder, inputData.orderArr);
	return 0;
}