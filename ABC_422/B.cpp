#include <iostream>
#include <string>

using namespace std;

int main() {
	int h, w;
	cin >> h >> w;
	int board[h][w];
	for(int i = 0; i < h; i++) {
		string s;
		cin >> s;
		for(int j = 0; j < w; j++) {
			if (s[j] == '#') board[i][j] = 1;
			else board[i][j] = 0;
		}
	}

	bool valid = true;
	for(int i = 0; i < h; i++) {
		for(int j = 0; j < w; j++) {
			int count = 0;
			if(board[i][j] == 1) {
				if(i != 0 && board[i - 1][j] == 1) ++count;
				if(i + 1 != h && board[i + 1][j] == 1) ++count;
				if(j != 0 && board[i][j - 1] == 1) ++count;
				if(j + 1 != w && board[i][j + 1] == 1) ++count;
				if(count != 2 && count != 4) {
					valid = false;
					break;
				}
			}
		}
	}
	cout << (valid ? "Yes" : "No") << endl;
	return 0;
}