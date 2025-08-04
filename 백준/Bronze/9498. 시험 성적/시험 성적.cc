#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int score;
    cin >> score;
    if(90<= score) cout << "A";
    else if(80<= score and score <= 89) cout << "B";
    else if(70<= score and score <= 79) cout << "C";
    else if(60<= score and score <= 69) cout << "D";
    else cout <<"F";
    }