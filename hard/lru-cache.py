#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
参考 https://www.cnblogs.com/zuoyuan/p/3701572.html
基于"最近用到的数据被重用的概率比较早用到的大的多"这样一个理念来设计的LRU算法，使用了双向链表（双向链表是环形的）
List的元素是Node格式的，而LRUCache就是在List基础上处理元素的get和put操作
"""
class List(object):
    @staticmethod
    def delete(elem): # 删除存储中的元素elem，elem类型为Node类型
        elem.prev.next = elem.next
        elem.next.prev = elem.prev
        return elem

    @staticmethod
    def move(elem, new_prev, new_next): # 将elem插入到new_prev和new_next之间
        elem.prev = new_prev
        elem.next = new_next
        new_prev.next = elem
        new_next.prev = elem

    @staticmethod
    def append(head, elem): # 将elem元素插入到head的前面，head为双向链表的表头
        List.move(elem, head.prev, head)

    @staticmethod
    def is_empty(head):
        return head.prev == head.next == head

    @staticmethod
    def init_head(head):
        head.prev = head.next = head

class Node(object):
    def __init__(self, key, value, head):
        self.key = key
        self.value = value
        self.head = head
        self.prev = self.next = None

    def hit(self): # 将self也就是Node类型的元素从List中清除，并在List中将self插入到head的前面，最近一次访问的Node放在双向队列的最前面
        List.delete(self)
        List.append(self.head, self)

class LRUCache(object):
    def __init__(self, capacity):
        """
        :param capacity: int
        """
        self.d = {} # 元素集合
        self.cap = capacity
        self.head = Node(-1, -1, None)
        List.init_head(self.head)

    def get(self, key):
        """
        :param key: int
        :return: int
        """
        if key not in self.d:
            return -1
        self.d[key].hit() # 最近一次查询的Node放在双向队列的前面
        return self.d[key].value

    def put(self, key, value):
        """
        :param key: int
        :param value: int
        :return: None
        """
        if self.cap == 0:
            return
        if key in self.d:
            self.d[key].hit() # 最近一次放入的的Node放在双向队列的最前面
            self.d[key].value = value
        else:
            if len(self.d) >= self.cap:
                old_node = List.delete(self.head.next)
                del self.d[old_node.key]
            new_node = Node(key, value, self.head)
            List.append(self.head, new_node)
            self.d[key] = new_node