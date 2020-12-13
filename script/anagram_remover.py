#!/usr/bin/env python3
"""
Service to remove anagrams in a list of strings
"""


def are_anagram(str1, str2):
    # Get lengths of both strings
    n1 = len(str1)
    n2 = len(str2)

    # If length of both strings is not same, then
    # they cannot be anagram
    if n1 != n2:
        return False

    # Sort both strings
    str1 = sorted(str1)
    str2 = sorted(str2)

    # Compare sorted strings
    for i in range(0, n1):
        if str1[i] != str2[i]:
            return False
    return True


def script_runner():
    input_l = ["poke", "pkoe", "okpe", "ekop"] #["eat", "tea", "tan", "ate", "nat", "bat"]
    print(input_l)
    size = len(input_l)
    print(size)
    cp = input_l
    for i in range(len(cp)):
        if i == len(cp):
            break
        for j in range(len(cp)):
            if i == j:
                continue
            if j >= len(cp):
                break
            if i >= len(cp):
                break
            print(i, j)
            s1 = cp[i]
            s2 = cp[j]
            if are_anagram(s1, s2):
                s = s2 if i < j else s1
                input_l.remove(s)
                print("cp : ", cp)

    print("Anagrams removed : ", sorted(input_l))


if __name__ == '__main__':
    script_runner()