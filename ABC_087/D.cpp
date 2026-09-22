#include <iostream>
#include <vector>
#include <array>

using namespace std;
using ll = long long;
using ai = array<int, 2>;

bool valid = true;

void dfs(vector<vector<ai>>& edges, vector<int>& weights, int curr) {
	if(!valid)
		return;

	int w = weights[curr];
	
	for(auto arr: edges[curr]) {
		int v = arr[0];
		int d = arr[1];
		if(weights[v] == -1) {
			weights[v] = w + d;
			dfs(edges, weights, v);
		} else if (w + d != weights[v]) {
			valid = false;
			return;
		}
	}
}


int main() {
	int n, m; cin >> n >> m;
	vector<vector<ai>> edges(n + 1);
	vector<int> indegree(n + 1);
	for(int i = 0; i < m; i++) {
		int l, r, d; cin >> l >> r >> d;
		edges[l].push_back({r, d});
		indegree[r]++;
	}

	vector<int> weights(n + 1, -1);
	for(int i = 1; i <= n; i++) {
		if(indegree[i] == 0) {
			weights[i] = 0;
			dfs(edges, weights, i);
		}
	}

	for(int weight: weights) {
		cout << weight << ' ';
	}
	cout << '\n';

	for(int i = 1; i <= n; i++) {
		if(weights[i] > 1000000000 || weights[i] == -1)
			valid = false;
	}

	if(valid) {
		cout << "Yes" << endl;
	} else {
		cout << "No" << endl;
	}
	return 0;
}