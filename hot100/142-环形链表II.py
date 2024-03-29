#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

# 不允许修改 链表。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/linked-list-cycle-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#

# 第一次相遇属于上一道题情况
# 第二次相遇在链表环入口位置处
def detectCycle(head):
    if not head or not head.next:
        return None
    
    slow = head
    fast = head.next
    while True:
        if not fast or not fast.next:
            return None
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow


# 0 0 0 0 0 0 0 0 
#         0     0
#         0 0 0 0
