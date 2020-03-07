#!/usr/bin/env python
# -*- coding: utf-8 -*-


def votes_sort(votes):
    if not votes or len(votes) <= 1:
        return votes
    votes_num = len(votes)
    person_num = len(votes[0])
    person_map = {}
    for i in range(person_num): 
        for j in range(votes_num):
            if votes[j][i] not in person_map:
                person_map[votes[j][i]] = 1
            else:
                person_map[votes[j][i]] += 1
        person_map = sorted(person_map.items(), key= lambda x: x[1], reverse=True)
        

        for k in range(len(person_map)):
            person_map[k]

if __name__ == "__main__":
    votes = ["ABC","CAB","BAC","BCA","ACB"]
    votes_sort(votes)