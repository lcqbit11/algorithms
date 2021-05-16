#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.listNode import ListNode, show_list_node


def reverse_nodes_in_k_group(head, k):
    """
    给定一个链表，和一个正整数k，按照顺序每次反转链表中的k个元素，
    如果链表的元素个数不是k的整数倍，那么剩余的不满k个的节点保持不变，并返回修改后的链表。
    :param head: ListNode
    :return: ListNode
    """
    def reverse_link_list(pre, next):
        last = pre.next  # last表示已完成反转的序列中最后一个node
        cur = last.next  # cur表示即将参与反转的node，肯定是last的下一个node
        while cur != next:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
        return last

    def reverse_link_list1(pre, next):
        last = pre.next
        res = last
        cur = last.next
        last.next = None
        while cur != next:
            tmp = cur.next
            cur.next = last
            last = cur
            cur = tmp
        res.next = next
        pre.next = last
        return res

    dummy = ListNode(-1)
    pre = dummy
    cur = head
    dummy.next = head
    index = 0
    while cur:
        index += 1
        if index % k == 0:
            # 以这k个node的开始node的前一个node和结尾node的下一个node来做执行反转操作，
            # 并返回已反转薛列中的最后一个node
            pre = reverse_link_list1(pre, cur.next)
            cur = pre.next
        else:
            cur = cur.next
    return dummy.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = mid1 = ListNode(2)
    mid1.next = mid2 = ListNode(3)
    mid3 = mid2.next = ListNode(4)
    mid4 = mid3.next = ListNode(5)
    mid5 = mid4.next = ListNode(6)
    mid5.next = None

    k = 2
    res = reverse_nodes_in_k_group(head, k)
    print(show_list_node(res))