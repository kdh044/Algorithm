#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    
    int answer;
    
    answer = (1 << n) + 1;
    cout << answer * answer;
    
}