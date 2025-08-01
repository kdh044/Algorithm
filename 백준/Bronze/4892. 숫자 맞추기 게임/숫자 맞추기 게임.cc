#include <iostream>
using namespace std;

int main(){
    int n0;
    int case_num = 0;
    while(true){
        cin >> n0;
        case_num += 1;
        if(n0 == 0){
            break;
        }
        int n1 = 3 * n0;
        int n2,n3,n4;
        cout << case_num << ".";
        
       if (n1 % 2 ==0){
           cout << " even ";
           n2 = n1/2 ;
       }
       else{
           cout << " odd ";
           n2 = (n1+1)/2;
       }
           n3 = 3*n2;
           cout << n3/9 <<endl;
        
    }
    return 0;
}