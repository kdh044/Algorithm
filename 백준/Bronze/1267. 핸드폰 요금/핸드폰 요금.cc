#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int number, time[20] , Y[20] , M[20];
    int Y_sum = 0 , M_sum = 0;
    
    cin >> number;
    for(int i = 0; i < number; i++) cin >> time[i];
    
    for(int i = 0; i < number; i++) Y[i] = time[i] / 30 + 1;
    
    for(int i = 0; i < number; i++) Y_sum += Y[i] * 10;
    
    for(int i = 0; i < number; i++) M[i] = time[i] / 60 + 1;
    
    for(int i = 0; i < number; i++) M_sum += (M[i]) * 15;
        
    if(M_sum > Y_sum) cout << "Y" << " " << Y_sum;
    
    else if(M_sum < Y_sum) cout << "M" << " " <<M_sum;
    
    else cout << "Y M " << M_sum;
  
    
}