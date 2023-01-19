#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
"""
link list example:
    head = ListNode(1)
    head.next = mid1 = ListNode(2)
    mid1.next = mid2 = ListNode(3)
    mid3 = mid2.next = ListNode(4)
    mid4 = mid3.next = ListNode(5)
    mid5 = mid4.next = ListNode(6)
    mid5.next = None
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def show_list_node(head):
    res = ""
    while head:
        res += str(head.val) + '->'
        head = head.next
    return res[:-2]