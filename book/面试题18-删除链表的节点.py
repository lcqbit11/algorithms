#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.listNode import ListNode

def delete_node(head, node):
    """
    :param head: ListNode
    :param node: ListNode
    :return: ListNode
    """
    if node.next:
        temp = node.next
        node.val = temp.val
        node.next = temp.next
        del temp
    elif head == node:
        head = None
    else:
        temp = head
        next_node = temp.next
        while next_node.next:
            temp = temp.next
            next_node = next_node.next
        temp.next = None
        del next_node

    return head

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

    result = delete_node(head, head_3)

    while result:
        print(result.val)
        result = result.next