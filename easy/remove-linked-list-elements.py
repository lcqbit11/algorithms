#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.listNode import ListNode, show_list_node


def removeLinkedElements(head, val):
    """
    从链表中删除节点值等于val的所有元素。
    :param head: ListNode(int)
    :param val: int
    :return: ListNode(int)
    """
    if not head:
        return
    dumpy = ListNode(-1)
    dumpy.next = head
    q = dumpy
    p = q.next
    while p:
        if p.val == val:
            q.next = p.next
            p = p.next
        else:
            q = q.next
            p = p.next
    return dumpy.next


if __name__ == '__main__':
    head = ListNode(1)
    node1 = ListNode(4)
    node2 = ListNode(3)
    node3 = ListNode(4)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = None

    print(show_list_node(head))
    head = removeLinkedElements(head, 4)
    print(show_list_node(head))