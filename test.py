#!/usr/bin/env python3

from string import ascii_lowercase

medical = open('medical.txt', 'r').read().splitlines()
initials = list(map(lambda s: s[0], medical))
print('Missing the following initials:')
for c in ascii_lowercase:
    if c not in initials:
        print(c, end='')
