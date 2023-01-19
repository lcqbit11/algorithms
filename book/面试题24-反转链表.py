#!/usr/bin/emv python
# -*- coding: utf-8 -*-
from utils.listNode import ListNode, show_list_node


def reverse_linklist(head):
    """
    :param head: ListNode(int)
    :return: ListNode(int)
    """
    dummy = ListNode(-1)
    dummy.next = head
    pre = dummy
    cur = pre.next
    next = cur.next
    while next:
        cur.next = next.next
        next.next = pre.next
        pre.next = next
        next = cur.next

    return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = mid1 = ListNode(2)
    mid1.next = mid2 = ListNode(3)
    mid3 = mid2.next = ListNode(4)
    mid4 = mid3.next = ListNode(5)
    mid5 = mid4.next = ListNode(6)
    mid5.next = None

    print(show_list_node(reverse_linklist(head)))