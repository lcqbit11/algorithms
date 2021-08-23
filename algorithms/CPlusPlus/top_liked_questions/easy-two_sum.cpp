#include<iostream>
#include<vector>
#include<unordered_map>

using namespace std;

//leetcodeurl https://leetcode.com/problems/two-sum/
class Solution {
public:
    vector<int> test(vector<int>& nums, int target);
};

vector<int> Solution::test(vector<int>& nums, int target) {
    vector<int> res;
    unordered_map<int, int> mp;
    for (int i = 0; i < nums.size(); i++) {
        int tmp = target - nums[i];
        if (mp.find(tmp) != mp.end()) {
            res.push_back(mp[tmp]);
            res.push_back(i);
        } else {
            mp[nums[i]] = i;
        }
    }

    return res;
}