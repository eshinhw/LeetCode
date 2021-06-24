#include <vector>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = nums[0];
        int currSum = 0;

        for (int num : nums) {
            if (currSum < 0) {
                currSum = 0;
            }

            currSum += num;

            maxSum = max(currSum, maxSum);

        }

        return maxSum;
    }
};