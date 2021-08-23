#include<iostream>
#include<vector>
#include<unordered_map>
#include "../test/utils.h"

using namespace std;

//leetcode url https://leetcode.com/problems/median-of-two-sorted-arrays
class Solution {
public:
    double test(vector<int>& nums1, vector<int>& nums2);
    double find_median(vector<int>& nums1, vector<int>& nums2, int k);
};

double Solution::test(vector<int>& nums1, vector<int>& nums2) {
    int len1 = nums1.size();
    int len2 = nums2.size();
    int len_sum = len1 + len2;
    if (len_sum % 2 == 1) {
        return find_median(nums1, nums2, len_sum/2 + 1);
    } else {
        return (find_median(nums1, nums2, len_sum/2) + find_median(nums1, nums2, len_sum/2 + 1))/2.0;
    }
}

double Solution::find_median(vector<int>& nums1, vector<int>& nums2, int k) {
    int len1 = nums1.size();
    int len2 = nums2.size();
    if (len1 > len2) {
        return find_median(nums2, nums1, k);
    }
    if (len1 == 0) {
        return nums2[k-1];
    }
    if (k == 1) {
        return max(nums1[0], nums2[0]);
    }
    int l1_index = min(k/2, len1);
    int l2_index = k - l1_index;
    if (nums1[l1_index-1] < nums2[l2_index-1]) {
        vector<int> nums1_new;
        for (int j = l1_index; j < len1; j++) {
            nums1_new.push_back(nums1[j]);
        }
        return find_median(nums1_new, nums2, k - l1_index);
    } else if (nums1[l1_index-1] > nums2[l2_index-1]) {
        vector<int> nums2_new;
        for (int j = l2_index; j < len2; j++) {
            nums2_new.push_back(nums2[j]);
        }
        return find_median(nums1, nums2_new, k - l2_index);
    } else {
        return nums1[l1_index - 1];
    }
}