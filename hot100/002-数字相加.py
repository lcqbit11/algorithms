#!/usr/bin/env python
# -*- coding: utf -*-
from util.listNode import ListNode, generate_node_list, show_list_node


##
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#

def addTwoNumbers(l1, l2):
    l = ListNode(-1)
    dump = l

    up_bit = 0
    while l1 and l2:
        value = (l1.val + l2.val + up_bit) % 10
        up_bit = (l1.val + l2.val + up_bit) // 10
        l1 = l1.next
        l2 = l2.next
        node = ListNode(value)
        l.next = node
        l = l.next

    rest = l1 if l1 else l2
    while rest:
        value = (rest.val + up_bit) % 10
        up_bit = (rest.val + up_bit) // 10
        rest = rest.next
        node = ListNode(value)
        l.next = node
        l = l.next

    if up_bit:
        l.next = ListNode(up_bit)

    return dump.next


if __name__ == "__main__":
    # l1 = [2, 4, 3]
    # l2 = [5, 6, 4]
    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    head1 = generate_node_list(l1)
    head2 = generate_node_list(l2)
    print(show_list_node(head1))
    print(show_list_node(head2))

    res = addTwoNumbers(head1, head2)
    print(show_list_node(res))

