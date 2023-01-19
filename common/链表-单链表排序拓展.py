#!/usr/bin/env python
# -*- coding:utf-8 -*-

from utils.listNode import ListNode

def linked_list_every_k_reverse(head):
    """
    单链表中，每k个节点进行倒序的操作，但是每k个节点之间的相对顺序不发生改变，输出这样操作后的链表
    :param head: ListNode
    :return: ListNode
    """
    def reverse_node(head_in):
