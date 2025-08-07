#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    
    vector<int> arr;
    
    while(n--){
        string str;
        cin >> str;
        
        if(str == "push"){
            int a;
            cin >> a;
            arr.push_back(a);
        }
        else if(str == "pop"){
            if (arr.empty()) cout << -1 << "\n";
            
            else {
             cout << arr.back() << "\n";
             arr.pop_back();    
            }
        }
        else if(str == "size"){
            cout << arr.size() << "\n";
        }
        else if(str == "empty"){
            cout << arr.empty() << "\n";
        }
        else {
            if (arr.empty()) cout << -1 << "\n";
            else cout << arr.back() << "\n";
        }
    }
}