#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.listNode import ListNode, show_list_node


def swap_nodes_pairs(head):
    """
    给定一个链表，将每两个相邻的节点进行交换，并返回结果的头节点。
    :param head: ListNode(int)
    :return: ListNode(int)
    """
    if not head or not head.next:
        return head
    dumpy = ListNode(-1)
    dumpy.next = head
    current = dumpy

    first = current.next
    second = first.next
    while second:
        first.next = second.next
        second.next = first
        current.next = second

        current = current.next.next
        if current.next and current.next.next:
            first = current.next
            second = first.next
        else:
            break

    return dumpy.next


def swap_nodes_pairs1(head):
    if not head or not head.next:
        return head

    dumpy = ListNode(-1)
    dumpy.next = head
    pre = dumpy
    cur = pre.next
    while cur and cur.next:
        next = cur.next

        cur.next = next.next
        next.next = cur
        pre.next = next

        pre = pre.next.next
        cur = pre.next

    return dumpy.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = mid1 = ListNode(2)
    mid1.next = mid2 = ListNode(3)
    mid3 = mid2.next = ListNode(4)
    mid4 = mid3.next = ListNode(5)
    mid5 = mid4.next = ListNode(6)
    mid5.next = None

    print(show_list_node(swap_nodes_pairs1(head)))