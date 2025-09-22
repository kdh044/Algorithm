#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    
    cin >> n;
    string s;
    
    while(n--){
        cin >> s;
        
        if(s.find('S') != string::npos ) break; //C++선택한 나를 죽이고싶다 씨발.
        //if(count(s.begin(),s.end(),s) > 0) break; 이것도됨
    }
    cout << s;
    
    
}