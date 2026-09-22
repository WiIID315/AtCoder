// Online C++ compiler to run C++ program online
#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool found = false;
int h, w;
vector<vector<vector<bool>>>dp;
vector<char> path;
int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
char letters[4] = {'D', 'U', 'R', 'L'};

void dfs(int r, int c, int dir, vector<string>& mat) {
    if(found || r < 0 || r >= h || c < 0 || c >= w || dp[r][c][dir]) {
        return;
    }
    dp[r][c][dir] = true;
    if(mat[r][c] == 'G') {
        found = true;
        return;
    }
    if(mat[r][c] == '#')
        return;
    else if(mat[r][c] == 'o') {
        path.push_back(letters[dir]);
        dfs(r + dirs[dir][0], c + dirs[dir][1], dir, mat);
        if(found) return;
        path.pop_back();
    } else if(mat[r][c] == 'x'){
        for(int i = 0; i < 4; i++) {
            if(i != dir) {
                path.push_back(letters[i]);
                dfs(r + dirs[i][0], c + dirs[i][1], i, mat);
                if(found) return;
                path.pop_back();
            }
        }
    } else {
        for(int i = 0; i < 4; i++) {
            path.push_back(letters[i]);
            dfs(r + dirs[i][0], c + dirs[i][1], i, mat);
            if(found) return;
            path.pop_back();
        }
    }
}

void solve() {
    cin >> h >> w;
    vector<string> mat;
    int sr = 0;
    int sc = 0;
    int er = 0;
    int ec = 0;
    for(int i = 0; i < h; i++) {
        string s; cin >> s;
        if(s.find('S') != -1) {
            sr = i;
            sc = s.find('S');
        }
        if(s.find('G') != -1) {
            er = i;
            ec = s.find('G');
        }
        mat.push_back(s);
    }
    
    dp = vector<vector<vector<bool>>>(h, vector<vector<bool>>(w, vector<bool>(4, false)));
    dfs(sr, sc, 0, mat);
    if(found) {
        cout << "Yes" << '\n';
        for(auto c: path) {
            cout << c;
        }
        cout << '\n';
    } else {
        cout << "No" << '\n';
    }
}

int main() {
    cin.tie(0) -> sync_with_stdio(0);
    solve();

    return 0;
}