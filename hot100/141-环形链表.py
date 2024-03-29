#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# 给你一个链表的头节点 head ，判断链表中是否有环。

# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

# 如果链表中存在环 ，则返回 true 。 否则，返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/linked-list-cycle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


# 使用 Floyd 判圈算法, 又称龟兔赛跑算法
def hasCycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        
        slow = slow.next
        fast = fast.next.next
    
    return True
