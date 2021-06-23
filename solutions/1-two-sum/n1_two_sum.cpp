#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        map<int,int> loc = {};
        vector<int> res = {};

        for (int i=0; i < nums.size(); i++) {
            int remainder = target - nums[i];

            if (loc.find(remainder) == loc.end()) {
                loc[nums[i]] = i;
            } else {
                res.push_back(loc[remainder]);
                res.push_back(i);
                return res;
            }
        }

        return res;
    }
};