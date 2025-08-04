#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> v(9);
    for(int i = 0; i < 9; i++) cin >> v[i]; 

    auto it = max_element(v.begin(),v.end()); 
    cout << *it << "\n";
    cout << (it - v.begin()+1);
}
