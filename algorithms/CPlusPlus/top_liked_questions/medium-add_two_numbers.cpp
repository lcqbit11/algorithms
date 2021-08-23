#include<iostream>
#include<vector>
#include<unordered_map>
#include "../test/utils.h"

using namespace std;

// leetcode url https://leetcode.com/problems/add-two-numbers/
class Solution {
public:
    ListNode* test(ListNode* l1, ListNode* l2);
};

ListNode* Solution::test(ListNode* l1, ListNode* l2) {
    int carry = 0;
    int num1 = 0, num2 = 0;
    ListNode* res = new ListNode(0);
    ListNode* link = res;
    while (l1 != NULL || l2 != NULL) {
        if (l1 != NULL) {
            num1 = l1->val;
            l1 = l1->next;
        }
        if (l2 != NULL) {
            num2 = l2->val;
            l2 = l2->next;
        }

        int v = num1 + num2 + carry;
        ListNode* newnode = new ListNode(v % 10);
        link->next = newnode;
        link = link->next;
        carry = v / 10;

        num1 = 0;
        num2 = 0;
    }
    if (carry > 0) {
        ListNode* newnode = new ListNode(carry);
        link->next = newnode;
    }

    return res->next;
}