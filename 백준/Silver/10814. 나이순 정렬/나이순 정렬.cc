#include <bits/stdc++.h>
using namespace std;

#define x first
#define y second
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    vector<pair<int,string>> members(n);
    for (int i = 0; i < n; i++) {
        cin >> members[i].first >> members[i].second;
    }
    
    stable_sort(members.begin(),members.end(), [](const auto &a, const auto &b){
        return a.first < b.first;
    });
    
     for (auto &m : members) {
        cout << m.first << ' ' << m.second << '\n';
    }
}