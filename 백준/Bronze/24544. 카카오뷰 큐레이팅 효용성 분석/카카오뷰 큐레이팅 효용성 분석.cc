#include <iostream>
using namespace std;

int main(){
    int num;
    cin >> num;
    int total_score = 0;
    int first_register = 0;
    int scores[1000];
    int visits[1000];
    
    
    for(int i=0; i<num; i++){
        cin >> scores[i];
        total_score += scores[i];
    }
    for(int i=0; i<num; i++){
        cin >> visits[i];
        if (visits[i] == 0){
            first_register += scores[i];
        }
    }  
    cout << total_score << "\n" << first_register;
}

