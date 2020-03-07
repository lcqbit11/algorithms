#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bm_match(s, part_s):
    """
    :param s: str
    :param part_s: str
    :return: match_index
    """
    def find_good_part(p, k, n):
        index = k
        for i in range(n - k + 1):
            if p[i] != p[index]:
                return -1
            index += 1
        return n - k

    def find_reverse_index(q, index, c):
        for i in reversed(range(0, index + 1)):
            if q[i] == c:
                return i
        return -1

    l_s = len(s)
    l_part_s = len(part_s)
    cur_end = l_part_s - 1
    while cur_end < l_s:
        temp = cur_end
        for i in reversed(range(0, l_part_s)):
            if part_s[i] != s[temp]:
                bad_rule = i - find_reverse_index(part_s[:i], i - 1, s[temp])
                if i < l_part_s - 1:
                    good_rule = i - find_good_part(part_s, i + 1, l_part_s - 1)
                else:
                    good_rule = 0
                print("cur_end_{}_index_{}".format(cur_end, i), "bad_rule:", bad_rule, ',', "good_rule:", good_rule)
                cur_end += max(bad_rule, good_rule)
                break
            temp -= 1
        else:
            return cur_end
    return -1


if __name__ == "__main__":
    s = "BBC ABCDABD ABCDAB ABCDABCDABDE"
    part_s = "ABCDABD"
    print(len(s))
    print(len(part_s))
    print(bm_match(s, part_s))