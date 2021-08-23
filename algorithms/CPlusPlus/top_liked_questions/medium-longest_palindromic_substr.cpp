#include<iostream>
#include<vector>
#include<unordered_map>

using namespace std;


// leetcode url https://leetcode.com/problems/longest-palindromic-substring/
class Solution {
public:
    string test(string s) {
        if (s.empty()) {
            return "";
        }

        int n = s.size();
        int j = 0;
        int max_len = 0;
        string res = "";
        for (int i = 0; i < n; i++) {
            // 回文串长度为奇数
            j = 0;
            while (i - j >= 0 && i + j < n) {
                if (s[i-j] == s[i+j]) {
                    if (max_len < 2*j+1) {
                        max_len = 2*j+1;
                        res = s.substr(i-j, 2*j+1);
                    }
                    j += 1;
                } else {
                    break;
                }
            }

            // 回文串长度为偶数
            j = 0;
            while (i - j >= 0 && i + 1 + j < n) {
                if (s[i-j] == s[i+1+j]) {
                    if (max_len < 2*(j+1)) {
                        max_len = 2*(j+1);
                        res = s.substr(i-j, 2*(j+1));
                    }
                    j += 1;
                } else {
                    break;
                }
            }
        }

        return res;
    }
};