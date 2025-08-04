#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    vector<int> v(21);
    for (int i = 1; i <= 20; i++) v[i] = i; //1부터 20까지 카드 배열생성
    
    for (int i = 0; i < 10; i++) {
        int a, b;
        cin >> a >> b;
        reverse(v.begin() + a, v.begin() + b + 1);
    }
    
    for (int i = 1; i < 21; i++){
        cout << v[i] << " "; }
}
