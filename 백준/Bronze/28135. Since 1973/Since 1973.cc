#include <iostream>
#include <string>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int N;
    std::cin >> N;

    int count = 0;

    for (int i = 1; i < N; ++i) {
        count++; 
        std::string s = std::to_string(i);
        if (s.find("50") != std::string::npos) {
            count++; 
        }
    }

    std::cout << count + 1 << "\n";

    return 0;
}
