#!/usr/bin/env python
# -*- coding: utf-8 -*-


def print_list_node(head):
    while head:
        print(str(head.val), end='')
        head = head.next
        if head:
            print('->', end='')
        else:
            print()