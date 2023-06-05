#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。#

from utils.listNode import ListNode


def isPalindrome(head):
    def find_middle_link(head):
        if not head:
            return head
        
        pre = ListNode(-1)
        pre.next = head
        
        low = pre
        fast = pre
        while low and fast:
            low = low.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        return low

    def reverse_link(head):
        if not head:
            return head
        
        cur = head
        p = None
        while cur:
            tmp = cur.next
            cur.next = p
            p = cur
            cur = tmp
        
        return p
    

    mid = find_middle_link(head)
    reverse_head = reverse_link(mid)

    fist_half = head
    second_half = reverse_head
    while second_half:
        if fist_half.val != second_half.val:
            return False
        fist_half = fist_half.next
        second_half = second_half.next
    
    mid.next = reverse_link(reverse_head)
    return True


def isPalindrome_2(head):
    if not head:
        return head
    
    p = None
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        tmp = slow.next
        slow.next = p
        p = slow
        slow = tmp
    
    if fast:
        slow = slow.next
    
    while slow:
        if slow.val != p.val:
            return False
        slow = slow.next
        p = p.next
    
    return True
