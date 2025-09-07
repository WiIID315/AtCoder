#include <iostream>
#include <string>

using namespace std;

void solve() {
	int a, b, c;
	cin >> a >> b >> c;
	int total = 0;
	total += min(a, min(b, c));
	a -= total;
	b -= total;
	c -= total;
	if(a > 0 && c > 0) {
		int high = max(a, c);
		int low = min(a, c);
		int choice = min(low, high - low);
		total += choice;
		high -= 2 * choice;
		low -= choice;
		if(high > 0 && low > 0) total += 2 * (max(high, low) / 3);
	}
	cout << total << endl;
}

int main() {
	int t;
	cin >> t;
	while(t-- > 0) solve();
	return 0;
}