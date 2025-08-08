#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    while (n--){
        int k;
        string s;
        cin >> k >> s;
        for(auto c : s){
            for(int i = 0; i < k; i++)
                cout << c;
        }
       cout << "\n";
    }
    

}