#include<iostream>
#include<vector>

using namespace std;


class Solution {
public:
    // bool camp(int v1, int v2) {
    //     return to_string(v1)+to_string(v2) < to_string(v2)+to_string(v1);
    // }

    string test (vector<int>& nums) {
        int n = nums.size();
        // sort(nums.begin(), nums.end(), camp);
        // 自定义排序
        for (int i = 0; i < n ; i++) {
            for (int j = 0; j < n-1-i; j++) {
                if (std::to_string(nums[j])+std::to_string(nums[j+1]) < std::to_string(nums[j+1])+std::to_string(nums[j])) {
                    nums[j] = nums[j] + nums[j+1];
                    nums[j+1] = nums[j] - nums[j+1];
                    nums[j] = nums[j] - nums[j+1];
                }
            }
        }

        string res = "";
        for (int i = 0; i < n; i++) {
            res += std::to_string(nums[i]);
        }

        return res;
    }

};