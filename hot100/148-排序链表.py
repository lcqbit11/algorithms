#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。#

from utils.listNode import ListNode


def sortList(head):
    def merge(l1, l2):
        dumpy = ListNode(-1)
        temp = dumpy
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        elif l2:
            temp.next = l2
        
        return dumpy.next
    
    def sort(head, tail):
        if not head:
            return head
        
        if head.next == tail:
            head.next = None
            return head
        
        slow = head
        fast = head
        while fast != tail:
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next
        
        mid = slow
        return merge(sort(head, mid), sort(mid, tail))
    
    return sort(head, None)


# 时间复杂度O(nlongn), 空间复杂度O(1)
def sortList_2(head):
    def merge(l1, l2):
        dumpy = ListNode(0)
        temp = dumpy
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        elif l2:
            temp.next = l2
        
        return dumpy.next
    
    if not head:
        return head
    length = 0
    p = head
    while p:
        length += 1
        p = p.next

    dumpy = ListNode(0)
    dumpy.next = head
    sub_len = 1
    while sub_len < length:
        pre = dumpy
        cur = dumpy.next
        while cur:
            head1 = cur
            for i in range(1, sub_len):
                if cur.next:
                    cur = cur.next
                else:
                    break
            
            head2 = cur.next
            cur.next = None
            cur = head2
            for i in range(1, sub_len):
                if cur and cur.next:
                    cur = cur.next
                else:
                    break

            sub_node = None
            if cur:
                sub_node = cur.next
                cur.next = None
            
            merged_head = merge(head1, head2)
            pre.next = merged_head
            while pre.next:
                pre = pre.next
            cur = sub_node
        
        sub_len <<= 1
    
    return dumpy.next
