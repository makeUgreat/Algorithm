#include <iostream>
using namespace std;

int main() {
    int price;
    cin >> price;
    
    int coins[] = {500, 100, 50, 10 ,5, 1};
    int cnt = 0;
    int change = 1000 - price;
    
    for (int coin : coins) {
        cnt += change / coin;
        change %= coin;
    }
    
    cout << cnt << endl;
    return 0;
}