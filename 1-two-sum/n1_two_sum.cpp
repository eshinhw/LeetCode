#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        map<int, int> loc;
        int remainder;
        vector<int> output;

        for (int i=0; i < nums.size(); i++) {
            remainder = target - nums[i];

            if (loc.find(remainder) == loc.end()) {
                loc[remainder] = i
            } else {
                output.push_back(loc[remainder]);
                output.push_back(i);
                return output;
            }


        }

    }
};