#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.listNode import ListNode, show_list_node


def add_two_numbers_ii(l1, l2):
    """
    给定两个非空的链表表示两个非负整数，并且高位数字在前，请将两个整数加起来，
    并用链表返回其和，返回结果中也是高位数字在前。
    :param l1: ListNode(int)
    :param l2: ListNode(int)
    :return: ListNode(int)
    """
    # solution3
    s1 = []
    s2 = []
    while l1:
        s1.append(l1.val)
        l1 = l1.next
    while l2:
        s2.append(l2.val)
        l2 = l2.next
    res = ''
    carry = 0
    while s1 and s2:
        v = s1.pop() + s2.pop()
        carry, v = divmod(v + carry, 10)
        res = str(v) + res
    s = s1 if s1 else s2
    while s:
        carry, v = divmod(s.pop() + carry, 10)
        res = str(v) + res
    if carry:
        res = str(carry) + res

    dumpy = ListNode(-1)
    p = dumpy
    for i in range(len(res)):
        p.next = ListNode(int(res[i]))
        p = p.next
    return dumpy.next

    # solution2
    # s1 = ''
    # s2 = ''
    # divmod()
    # while l1:
    #     s1 += str(l1.val)
    #     l1 = l1.next
    # while l2:
    #     s2 += str(l2.val)
    #     l2 = l2.next
    # s = str(int(s1) + int(s2))
    # dumpy = ListNode(-1)
    # p = dumpy
    # for i in range(len(s)):
    #     p.next = ListNode(int(s[i]))
    #     p = p.next
    #
    # return dumpy.next

    # solution1
    # def reverse_list_node(h):
    #     cur = h
    #     pre = None
    #     while cur:
    #         tmp = cur.next
    #         cur.next = pre
    #         pre = cur
    #         cur = tmp
    #     return pre
    #
    # p = dummy = ListNode(-1)
    # p1, p2 = reverse_list_node(l1), reverse_list_node(l2)
    # carry = 0
    # while p1 and p2:
    #     p.next = ListNode(p1.val + p2.val + carry)
    #     if p.next.val >= 10:
    #         carry = 1
    #         p.next.val = p.next.val % 10
    #     else:
    #         carry = 0
    #     p1 = p1.next
    #     p2 = p2.next
    #     p = p.next
    # pp = p1 or p2
    # while pp:
    #     p.next = ListNode(pp.val + carry)
    #     if p.next.val >= 10:
    #         carry = 1
    #         p.next.val = p.next.val % 10
    #     else:
    #         carry = 0
    #     pp = pp.next
    #     p = p.next
    # head = reverse_list_node(dummy.next)
    # if carry:
    #     tmp = ListNode(1)
    #     tmp.next = head
    #     head = tmp
    # return head


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

    head1 = ListNode(2)
    head1_2 = ListNode(5)
    head1_3 = ListNode(6)
    head1_4 = ListNode(9)
    # head1_5 = ListNode(4)
    head1.next = head1_2
    head1_2.next = head1_3
    head1_3.next = head1_4
    head1_4.next = None
    # head1_5.next = None

    tmp = add_two_numbers_ii(head, head1)
    print(show_list_node(tmp))