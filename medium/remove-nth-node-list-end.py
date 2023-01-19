#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.listNode import ListNode, show_list_node


def remove_nth_node_from_list_end(head, n):
    """
    给定一个链表，移除它的倒数第n位节点，并返回头节点。
    :param head: ListNode(int)
    :return: ListNode(int)
    """
    dumpy = ListNode(-1)
    dumpy.next = head
    p = q = dumpy
    index = 1
    while index <= n and p:
        p = p.next
        index += 1
    while p.next and q.next:
        q = q.next
        p = p.next
    q.next = q.next.next

    return dumpy.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = mid1 = ListNode(2)
    mid1.next = mid2 = ListNode(3)
    mid3 = mid2.next = ListNode(4)
    mid4 = mid3.next = ListNode(5)
    mid5 = mid4.next = ListNode(6)
    mid5.next = None

    res = remove_nth_node_from_list_end(head, 2)
    print(show_list_node(res))