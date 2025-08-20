#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    
    vector<int> tickets(n);
    for (int i = 0; i < n; i++) {
        cin >> tickets[i];
    }

    sort(tickets.begin(), tickets.end());

    int smallest_available_ticket = 1;

    for (int sold_ticket : tickets) {
        if (sold_ticket == smallest_available_ticket) {
            smallest_available_ticket++;
        }
        else if (sold_ticket > smallest_available_ticket) {
            break;
        }
    }

    cout << smallest_available_ticket << "\n";
}