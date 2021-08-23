#include<iostream>
#include<vector>
#include<unordered_map>

using namespace std;


// leetcode url https://leetcode.com/problems/longest-palindromic-substring/
class Solution {
public:
    string test (vector<int>& nums) {
        int n = nums.size();
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
        if (nums[0] == 0) {
            res = "0";
        }

        return res;
    }
};


int main() {
    // vector<int> nums; 
    // nums.push_back(2);
    // nums.push_back(7);
    // nums.push_back(11);
    // nums.push_back(15);
    // int target = 9;
    Solution solution; 
    // vector<int> res = solution.test(nums, target);
    // cout << res[0] << ' ' << res[1] << endl;
    // vector<int> nums; 
    // nums.push_back(2);
    // nums.push_back(4);
    // nums.push_back(3);
    // vector<int> nums2; 
    // nums2.push_back(5);
    // nums2.push_back(6);
    // nums2.push_back(4);
    // ListNode* l1 = listnode_gen(nums);
    // ListNode* l2 = listnode_gen(nums2);
    // ListNode* res = solution.test(l1, l2);
    // listnode_print(res);
    // string s = "pwwkew";
    // int res = solution.test(s);
    // cout << res << endl;

    // vector<int> nums1;
    // vector<int> nums2;
    // // nums1 = [1,2], nums2 = [3,4]
    // nums1.push_back(1);
    // nums1.push_back(2);
    // nums2.push_back(3);
    // nums2.push_back(4);
    // double res = solution.test(nums1, nums2);
    // cout << res << endl;
    // cout << 4/2 << endl;

    // vector<int> nums3;
    // vector<int> nums4;
    // nums3.push_back(1);
    // nums3.push_back(2);
    // nums3.push_back(3);
    // nums3.push_back(4);
    // cout << endl;
    // nums4.assign(nums3.begin()+1, nums3.begin()+2);
    // for (int i = 0; i <= nums3.size(); i++) {
    //     cout << nums3[i] << endl;
    // }
    // cout << endl;
    // for (int i = 0; i <= nums4.size(); i++) {
    //     cout << nums4[i] << endl;
    // }

    // string s = "abbac";
    // cout << 2 << endl;
    // string res = solution.test(s);
    // cout << 3 << endl;
    // cout << res << endl;

    vector<int> nums3;//[3,30,34,5,9]
    nums3.push_back(3);
    nums3.push_back(30);
    nums3.push_back(34);
    nums3.push_back(5);
    nums3.push_back(9);
    string res = solution.test(nums3);
    cout << res << endl;
}

