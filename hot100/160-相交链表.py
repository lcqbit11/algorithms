#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。#


def getIntersectionNode(headA, headB):
    p = headA
    q = headB
    while True:
        if not p and not q:
            return None
        
        if p == q:
            return p
        
        if p:
            p = p.next
        else:
            p = headB
        
        if q:
            q = q.next
        else:
            q = headA
