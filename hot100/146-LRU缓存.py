#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/lru-cache
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


class Node(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    

# 哈希表+双向链表
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.d = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def exit_move_node_2_tail(self, key):
        node = self.d[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key):
        if key not in self.d:
            return -1
        self.exit_move_node_2_tail(key)
        return self.d[key].value

    def put(self, key, value):
        if key in self.d:
            self.d[key].value = value
            self.exit_move_node_2_tail(key)
        else:
            if len(self.d) == self.capacity:
                self.d.pop(self.head.next.key)

                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            new_node = Node(key, value)
            self.d[key] = new_node
            new_node.prev = self.tail.prev
            new_node.next = self.tail
            new_node.prev.next = new_node
            self.tail.prev = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print(lRUCache.get(1))
print(lRUCache.get(2))
lRUCache.put(3, 3)
print(lRUCache.get(1))
print(lRUCache.get(2))
