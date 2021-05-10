#include <vector>

using namespace std;

class Solution {
public:
    int countPrimes(int n) {
        vector<bool> sieve(n + 1, true);
        int count = 0;

        for (int i = 2; i * i < n; i++) {
            if (sieve[i]) {
                for (int j = i; j * i < n; j++) {
                    sieve[j*i] = false;
                }
            }
        }

        for (int i=2; i < n; i++) {
            if (sieve[i]) { count++; }
        }

        return count;
    }
};