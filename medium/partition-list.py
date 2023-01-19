#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.listNode import ListNode, show_list_node


def partition_list(head, x):
    """
    给定一个链表和一个值x，使得划分的两个分区的结果为：所有比x值小的节点排在所有不小于x值的节点的前面，
    并且要保证在每个分区内，节点的相对位置跟原来保持不变。
    :param head: ListNode(int)
    :param x: int
    :return: ListNode(int)
    """
    dumpy1 = ListNode(-1)
    dumpy2 = ListNode(-1)
    head1 = dumpy1
    head2 = dumpy2

    while head:
        if head.val < x:
            head1.next = head
            head1 = head1.next
        else:
            head2.next = head
            head2 = head2.next
        head = head.next
    head2.next = None
    head1.next = dumpy2.next

    return dumpy1.next


def partition_list1(head, x):
    if not head or not head.next:
        return head
    new_head = ListNode(-1)
    new_head.next = head
    pre = new_head
    last = pre
    cur = head
    while cur:
        if cur.val < x:
            if last == pre:
                last = last.next
                pre = pre.next
                cur = cur.next
            else:
                tmp = cur.next
                pre.next = cur.next
                cur.next = last.next
                last.next = cur
                last = last.next
                cur = tmp
        else:
            pre = pre.next
            cur = cur.next

    return new_head.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = mid1 = ListNode(4)
    mid1.next = mid2 = ListNode(3)
    mid3 = mid2.next = ListNode(2)
    mid4 = mid3.next = ListNode(5)
    mid5 = mid4.next = ListNode(2)
    mid5.next = None

    print(show_list_node(head))
    print(show_list_node(partition_list(head, 3)))