#include<iostream>
#include<vector>
#include<unordered_map>
#include "../test/utils.h"

using namespace std;

// leetcode url https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution {
public:
    int test(string s);
};

int Solution::test(string s) {
    if (s.empty()) {
        return 0;
    }
    int res = 0;
    int start = 0;
    unordered_map<char, int> mp;
    for (int i = 0; i < s.size(); i++) {
        char curr_char = s[i];
        if (mp.find(curr_char) != mp.end()) {
            start = max(start, mp[curr_char] + 1);
        }
        mp[curr_char] = i;

        res = max(res, i - start + 1);
    }

    return res;
}