#include <iostream>
#include <algorithm>

using namespace std;

int max_moves(int a, int b, int c) {
    return max(b-a, c-b)-1;
}

int main() {
    int a, b, c;
    
    while (cin >> a >> b >> c) {
        cout << max_moves(a,b,c) << endl;
    }
    
    return 0;
}
