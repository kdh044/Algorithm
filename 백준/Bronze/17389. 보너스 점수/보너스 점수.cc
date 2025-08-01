#include <iostream>
using namespace std;

int main(){
    int n;
    string s;
    cin >> n;
    cin >> s;
    int a = 0;
    int sum = 0;
    int bonus = 0;
    for (char c : s){
        a++;
        if (c == 'X')
        {
            bonus = 0;
        }
        else
        {
            sum += a + bonus;
            bonus++;
        }       
    }
        cout << sum;
        return 0;
    }