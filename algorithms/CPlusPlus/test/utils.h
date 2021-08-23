#include<iostream>
#include<vector>
#include<string>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* listnode_gen(vector<int>& nums) {
    ListNode* res = new ListNode(0);
    ListNode* link = res;
    for (int i = 0; i < nums.size(); i++) {
        ListNode* newnode = new ListNode(nums[i]);
        link->next = newnode;
        link = link->next;
    }

    return res->next;
}

void listnode_print(ListNode* head) {
    string res;
    while (head != NULL) {
        res += to_string(head->val) + ' ';
        head = head->next;
    } 
    cout << res << endl;
}