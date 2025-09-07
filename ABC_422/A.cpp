#include <iostream>
#include <string>

using namespace std;

int main() {
	string s;
	cin >> s;
	char j = s[2] + 1;
	char i = s[0];
	if (j > '8') {
		i++;
		j = '1';
	}
	cout << i << '-' << j << endl;
	return 0;
}