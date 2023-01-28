#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.listNode import generate_node_list, show_list_node
from operator import attrgetter

##
# 给你一个链表数组，每个链表都已经按升序排列。
#
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。#


def mergeKLists(lists):
    if not lists:
        return
    sort_nodes = []
    for list in lists:
        head = list
        while head:
            sort_nodes.append(head)
            head = head.next
    if not sort_nodes or len(sort_nodes) == 0:
        return
    sort_nodes = sorted(sort_nodes, key=attrgetter("val"), reverse=False)
    for i, node in enumerate(sort_nodes):
        try:
            node.next = sort_nodes[i+1]
        except:
            node.next = None

    return sort_nodes[0]


# lists = [[1,4,5],[1,3,4],[2,6]]
lists = [[]]
node_lists = []
show_node_lists = []
for list in lists:
    show_node_lists.append(show_list_node(generate_node_list(list)))
    node_lists.append(generate_node_list(list))
print(show_node_lists)
print(show_list_node(mergeKLists(node_lists)))
