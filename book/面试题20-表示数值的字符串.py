#!/usr/bin/env python
# -*- coding: utf-8 -*-

def as_str_value(s):
    """
    表示数值的字符串遵循 A[.[B]][e|EC] 或者.B[e|EC]
    :param s: str
    :return: bool
    """
    has_e = False
    decimal = False
    signal = False
    for i in range(len(s)):
        if s[i] == 'E' or s[i] == 'e':
            if has_e: return False
            has_e = True
        elif s[i] == '+' or s[i] == '-':
            if signal and s[i-1] != 'E' and s[i-1] != 'e':
                return False
            if not signal and i>0 and s[i-1] != 'E' and s[i-1] != 'e':
                return False
            signal = True
        elif s[i] == '.':
            if has_e or decimal: return False
            decimal = True
        elif ord(s[i])-ord('0')<0 or ord(s[i])-ord('9')>0:
            return False

    return True

if __name__ == "__main__":
    s = "12e+4.3"
    print(as_str_value(s))