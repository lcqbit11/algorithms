#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.listNode import ListNode, show_list_node


def odd_even_linked_list(head):
    """
    给定一个单链表，请将所有的奇数位放在前面(1,3,5,,,)，偶数位放在后面(2,4,6,,,)，我们所说的奇数位和偶数位是指节点的位置而不是节点的数值。
    要求：在O(1)的空间复杂度和O(#nodes)的时间复杂度内完成。
    :param head: TreeNode(int)
    :return: TreeNode(int)
    """
    o = odd = ListNode(-1)
    e = even = ListNode(-1)
    p = head
    is_odd = True
    while p:
        if is_odd:
            o.next = p
            o = o.next
            is_odd = False
        else:
            e.next = p
            e = e.next
            is_odd = True
        p = p.next
    e.next = None
    o.next = even.next

    return odd.next


def odd_even_linked_list1(head):
    if not head or not head.next:
        return head
    odd = head
    even = head.next
    even_head = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head

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

    print(show_list_node(odd_even_linked_list1(head)))