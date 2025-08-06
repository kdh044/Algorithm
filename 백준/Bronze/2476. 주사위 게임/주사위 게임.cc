#include <bits/stdc++.h>
using namespace std;

int main(void){
    int n;
    cin >> n;
    int maximum = 0;
    
    for(int i = 0; i < n; i++){
        int a, b ,c;
        int sum;
        cin >> a >> b >> c;
        if(a == b and b == c){
            sum = 10000 + a * 1000;
        }
        else if(a == b or b == c){
            sum = 1000 + b * 100;
        }
        else if(a == c){
            sum = 1000 + a * 100;
        }
        else{
            sum = max({a,b,c}) * 100;
        }
        if(sum > maximum){
            maximum = sum;
        }
    }
    cout << maximum;
}