#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/word-search
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


def exist(board, word):
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


    def backtrack(i, j, mark, board, word):
        if len(word) == 0:
            return True
        
        for direct in directs:
            cur_i = direct[0] + i
            cur_j = direct[1] + j

            if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]):
                if board[cur_i][cur_j] == word[0]:
                    if mark[cur_i][cur_j] == 1:
                        continue
                    else:
                        mark[cur_i][cur_j] = 1
                        if backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
                            return True
                        else:
                            mark[cur_i][cur_j] = 0
        
        return False
                    
        
    if not board or not word:
        return False

    m, n = len(board), len(board[0])
    mark = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                mark[i][j] = 1
                if backtrack(i, j, mark, board, word[1:]) == True:
                    return True
                else:
                    mark[i][j] = 0
                
    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"
word = "SEE"
# word = "ABCB"
print(exist(board, word))
