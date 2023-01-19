#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.listNode import ListNode


def add_two_numbers(l1, l2):
    """
    给定两个链表，分别表示非负整数，且每个整数在链表中都是倒序存储，即低位数字在前，计算两个整数的和，
    并将他们按照倒叙存储到一个链表中
    example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
    :param l1: ListNode(int)
    :param l2: ListNode(int)
    :return: ListNode(int)
    """
    dumpy1 = ListNode(-1)
    dumpy2 = ListNode(-1)
    dumpy = ListNode(-1)
    dumpy1.next = l1
    dumpy2.next = l2
    p = dumpy1
    q = dumpy2
    res = dumpy
    upBit = 0
    while p.next and q.next:
        tmp = (p.next.val + q.next.val + upBit) % 10
        upBit = (p.next.val + q.next.val + upBit) // 10
        nextNode = ListNode(tmp)
        res.next = nextNode
        res = res.next
        p = p.next
        q = q.next

    k = p.next or q.next

    while k:
        tmp = (k.val + upBit) % 10
        upBit = (k.val + upBit) // 10
        nextNode = ListNode(tmp)
        res.next = nextNode
        res = res.next
        k = k.next

    if upBit:
        res.next = ListNode(upBit)

    output = []
    while dumpy.next:
        output.append(int(dumpy.next.val))
        dumpy = dumpy.next

    return output


if __name__ == '__main__':
    head = ListNode(1)
    node1 = ListNode(2)
    head.next = node1
    node2 = ListNode(3)
    node1.next = node2
    node3 = ListNode(4)
    node2.next = node3
    node3.next = None

    head1 = ListNode(4)
    node11 = ListNode(2)
    head1.next = node11
    node21 = ListNode(8)
    node11.next = node21
    node31 = ListNode(7)
    node21.next = node31
    node31.next = None

    resLink = add_two_numbers(head, head1)
    # res = ''
    # while resLink:
    #     res = res + str(int(resLink.val))
    #     resLink = resLink.next

    print(resLink)