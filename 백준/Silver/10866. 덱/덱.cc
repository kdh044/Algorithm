#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n ,x ;
    cin >> n;
    
    deque <int> dq;
    string str;
    while(n--){
        cin >> str;
        if (str == "push_front"){
            cin >> x; 
            dq.push_front(x);
        }
        else if(str == "push_back"){
            cin >> x;
            dq.push_back(x);
        }
        else if (str == "pop_front"){
            if(dq.empty()){
                cout << -1 << "\n";
            }
            else{
                cout << dq.front() << "\n";
                dq.pop_front();
            }
        }
        else if (str == "pop_back"){
            if(dq.empty()){
                cout << -1 << "\n";
            }
            else {
                cout << dq.back() << "\n";
                dq.pop_back();
          }
        }
        else if (str == "size"){
            cout << dq.size() << "\n";
        }
        else if (str == "empty"){
            cout << dq.empty() << "\n";
        }
        else if (str == "front"){
            if(dq.empty()){
                cout << -1 << "\n";
            }
            else{
                cout << dq.front() << "\n";
            }
        }
        else{
            if(dq.empty()){
                cout << -1 << "\n";
            }
            else{
                cout << dq.back() <<"\n";
            }
        }
               
           }
    }
