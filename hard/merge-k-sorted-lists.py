#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.listNode import ListNode
import heapq
from operator import attrgetter


def merge_k_sorted_lists(lists):
    """
    给定k个有序的链表，将他们组合成一个有序的链表
    :param lists: List(ListNode)
    :return: ListNode
    """
    # sorted_link_list = []
    # for head in lists:
    #     node = head
    #     while node:
    #         sorted_link_list.append(node)
    #         node = node.next
    # sorted_link_list = sorted(sorted_link_list, key=attrgetter('val'))
    # for i, cur in enumerate(sorted_link_list):
    #     try:
    #         cur.next = sorted_link_list[i + 1]
    #     except:
    #         cur.next = None
    #
    # if sorted_link_list:
    #     return sorted_link_list[0]
    # else:
    #     return None

    heap = []
    p = dummy = ListNode(-1)
    for i in range(len(lists)):
        node = lists[i]
        if not node:
            continue
        heapq.heappush(heap, (node.val, node))

    while heap:
        _, node = heapq.heappop(heap)
        p.next = node
        p = p.next
        if node.next:
            node = node.next
            heapq.heappush(heap, (node.val, node))
    return dummy.next


if __name__ == "__main__":
    data = []

    h1 = ListNode(1)
    h2 = ListNode(4)
    h3 = ListNode(5)
    h1.next = h2
    h2.next = h3
    h3.next = None

    l1 = ListNode(1)
    l2 = ListNode(3)
    l3 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = None

    d1 = ListNode(2)
    d2 = ListNode(6)
    d1.next = d2
    d2.next = None

    data.append(h1)
    data.append(l1)
    data.append(d1)

    print(merge_k_sorted_lists(data))