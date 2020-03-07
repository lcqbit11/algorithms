#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.listNode import ListNode

def backward_k_node(head, k):
    """
    :param head: ListNode
    :return: ListNode
    """
    first = second = head
    if not head:
        return
    while k > 0 and second:
        second = second.next
        k -= 1
    if k == 0 and not second:
        temp = ListNode(-1)
        temp.next = first.next
        del first
        return temp.next
    while second.next:
        first = first.next
        second = second.next
    temp = first.next
    first.next = temp.next
    del temp
    return head

if __name__ == "__main__":
    head = ListNode(1)
    head_2 = ListNode(2)
    head_3 = ListNode(3)
    head_4 = ListNode(4)
    head_5 = ListNode(5)
    head.next = head_2
    head_2.next = head_3
    head_3.next = head_4
    head_4.next = head_5
    head_5.next = None

    temp = backward_k_node(head, 5)
    while temp:
        print(temp.val)
        temp = temp.next
    # print(backward_k_node(head, 2))