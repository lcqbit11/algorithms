#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.listNode import ListNode, show_list_node, generate_node_list

##
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
#  
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/remove-nth-node-from-end-of-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


def removeNthFromEnd(head, n):
    dump = ListNode(-1)
    dump.next = head
    p = dump
    q = dump
    index = 1
    while index <= n:
        p = p.next
        index += 1
    while p.next and q.next:
        p = p.next
        q = q.next
    q.next = q.next.next

    return dump.next


head = [1,2,3,4,5]
n = 2
print(show_list_node(generate_node_list(head)))
print(show_list_node(removeNthFromEnd(generate_node_list(head), n)))
