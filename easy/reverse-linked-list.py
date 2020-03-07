#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.listNode import ListNode, show_list_node


def reverse_linked_list(head):
    """
    单链表翻转
    :param head: ListNode(int)
    :return: reverse ListNode(int)
    """
    pre = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp

    return pre


def reverse_linked_list1(head):
    if not head:
        return
    dumpy = ListNode(-1)
    dumpy.next = head
    pre = dumpy
    cur = head
    while cur.next:
        ss = cur.next
        cur.next = ss.next
        ss.next = pre.next
        pre.next = ss

    return dumpy.next


if __name__ == '__main__':
    head = ListNode(1)
    node1 = ListNode(2)
    head.next = node1
    node2 = ListNode(3)
    node1.next = node2
    node3 = ListNode(4)
    node2.next = node3
    node3.next = None

    print(show_list_node(head))
    head = reverse_linked_list1(head)
    print(show_list_node(head))