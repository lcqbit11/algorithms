#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.listNode import ListNode, show_list_node, generate_node_list

##
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 #


def mergeTwoLists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    p = list1
    q = list2
    res = ListNode(-1)
    dump = res

    while p and q:
        if p.val < q.val:
            res.next = p
            res = res.next
            p = p.next
        else:
            res.next = q
            res = res.next
            q = q.next
    res.next = p if p else q

    return dump.next


l1 = [1,2,4]
l2 = [1,3,4]
print(show_list_node(generate_node_list(l1)))
print(show_list_node(generate_node_list(l2)))
print(show_list_node(mergeTwoLists(generate_node_list(l1), generate_node_list(l2))))
