#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/course-schedule
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#

from collections import deque

def canFinish(numCourses, prerequisites):
    indegress = [0 for _ in range(numCourses)]
    adjacency = [[] for _ in range(numCourses)]
    
    queue = deque()
    for cur, pre in prerequisites:
        indegress[cur] += 1
        adjacency[pre].append(cur)
    
    for i in range(numCourses):
        if not indegress[i]:
            queue.append(i)
    
    while queue:
        pre = queue.popleft()
        numCourses -= 1

        cur_list = adjacency[pre]
        for cur in cur_list:
            indegress[cur] -= 1
            if not indegress[cur]:
                queue.append(cur)
    
    return not numCourses


numCourses = 2
prerequisites = [[1,0]]
print(canFinish(numCourses, prerequisites))
