#/usr/bin/env python
# -*- coding: utf-8 -*-


def kmp_match(s, part_s):
    """
    :param s: str
    :param part_s: str
    :return: match_index
    """
    def gen_next(part_str):
        start, end = 0, 1
        result = [0] * len(part_str)
        while end < len(part_str):
            if part_str[start] == part_str[end]:
                start += 1
                end +=1
                result[end] = start
            elif start != 0:
                start = result[start-1]
            else:
                end += 1
        return result

    i = j = 0
    next_p = gen_next(part_s)
    while i < len(s) and j < len(part_s):
        if s[i] == part_s[j]:
            i += 1
            j += 1
        elif j != 0:
            j = next_p[j-1]
        else:
            i += 1
    if j == len(part_s):
        return i - j
    else:
        return -1


    # def partition_s(p):
    #     l_p = len(p)
    #     prefix_str = set()
    #     post_str = set()
    #     p_key = [0]
    #     for i in range(1, l_p):
    #         prefix_str.add(p[:i])
    #         post_str = {p[j:i + 1] for j in range(1, i + 1)}
    #         p_key.append(len((prefix_str & post_str or {''}).pop()))
    #     return p_key
    #
    # l_s = len(s)
    # l_part_s = len(part_s)
    # cur_begin = 0
    # part_key = partition_s(part_s)
    # while cur_begin < l_s - l_part_s:
    #     for i in range(l_part_s):
    #         if part_s[i] != s[cur_begin + i]:
    #             cur_begin += max(i - part_key[i - 1], 1)
    #             break
    #     else:
    #         return cur_begin
    # return -1


if __name__ == "__main__":
    s = "BBC ABCDAB ABCDABDABDE"
    part_s = "ABCDABD"
    print(kmp_match(s, part_s))