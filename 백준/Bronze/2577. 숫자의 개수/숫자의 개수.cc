#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int a,b,c,num;
    int arr[10] = {};
    cin >> a >> b >> c;
    num = a * b * c;
    string str = to_string(num);
    
    for(char c : str){
        arr[c - '0']++;
    }
    
    for(int i = 0; i < 10; i++){
        cout << arr[i] << "\n";
    }
}