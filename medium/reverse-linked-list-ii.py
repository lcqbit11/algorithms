#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.listNode import ListNode, show_list_node


def reverse_linked_list_ii(head, m, n):
    """
    给定一个链表，将位置m和位置n之间的节点进行逆序，其他保持不变，并返回头节点。
    :param head: ListNode[int]
    :param m: int
    :param n: int
    :return: ListNode[int]
    """
    dummy = ListNode(-1)
    dummy.next = head
    pre = dummy
    index = 1
    while index < m:
        pre = pre.next
        index += 1
    cur = pre.next
    next = cur.next
    while index < n:
        cur.next = next.next
        next.next = pre.next
        pre.next = next
        next = cur.next
        index += 1

    return dummy.next

    # def reverse_between_linked(cur, pre_end, k):
    #     tmp_start = cur
    #     pre = None
    #     next_node = None
    #     while cur and k > 0:
    #         next_node = cur.next
    #         cur.next = pre
    #         pre = cur
    #         cur = next_node
    #         k -= 1
    #     pre_end.next = pre  # m之前的nodes与该段的nodes连接
    #     tmp_start.next = next_node  # 该段的nodes连接与n之后的nodes连接
    #
    # dummy = ListNode(-1)
    # dummy.next = head
    # p = dummy
    # index = 1
    # start = None
    # while p:
    #     if index == m:  # m的前一个位置
    #         start = p   # m的前一个node
    #     if index == n + 1:  # 刚好n的位置
    #         reverse_between_linked(start.next, start, n-m+1)
    #         return dummy.next
    #     index += 1
    #     p = p.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = mid1 = ListNode(2)
    mid1.next = mid2 = ListNode(3)
    mid3 = mid2.next = ListNode(4)
    mid4 = mid3.next = ListNode(5)
    mid5 = mid4.next = ListNode(6)
    mid5.next = None

    m, n = 2, 5
    res = reverse_linked_list_ii(head, m, n)
    print(show_list_node(res))