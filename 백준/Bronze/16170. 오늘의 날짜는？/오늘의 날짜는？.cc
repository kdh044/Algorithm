#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    time_t t = time(0);
    tm* g = gmtime(&t);
    
        printf("%04d\n%02d\n%02d\n",
           g->tm_year + 1900,
           g->tm_mon + 1,
           g->tm_mday);
    return 0;
    
}