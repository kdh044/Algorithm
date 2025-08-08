#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    vector <int> a;
    int n;
    cin >> n;
    
    while(n--){
        int m;
        cin >> m;
        a.push_back(m);
    }
    cout << *min_element(a.begin(),a.end()) << " " << *max_element(a.begin(),a.end());
}