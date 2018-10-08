#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Nicolò Morando
'''


if __name__ == "__main__":
    wordlist = open("dictionary.txt", "r").read().split()
    words = open("scrambled-words.txt", "r").read().split()
    d = {}
    s = list()
    for word in words:
        chars = sorted(list(word))
        for compare in wordlist:
            if sorted(list(compare)) == chars:
                s.append(compare.lower())
    d["FLG"] = "".join(s)
    print(d)
