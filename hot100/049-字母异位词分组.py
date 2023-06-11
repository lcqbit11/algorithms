#!/usr/bin/env python
# -*- coding: utf-8 -*-


def groupAnagrams(strs):
    if not strs:
        return []
    
    new_list = []
    for s in strs:
        s = sorted(s)
        new_list.append(''.join(s))
    
    d = dict()
    for i in range(len(new_list)):
        key = new_list[i]
        value = strs[i]
        if key not in d:
            d[key] = [value]
        else:
            tmp = d[key]
            tmp.append(value)
            d[key] = tmp
    
    return list(d.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
