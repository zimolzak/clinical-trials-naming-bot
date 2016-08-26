#!/usr/bin/env python3

from string import ascii_lowercase

medical = open('medical.txt', 'r').read().splitlines()
positive = open('positive.txt', 'r').read().splitlines()

print('Missing the following initials:')
initials = list(map(lambda s: s[0], medical))
for c in ascii_lowercase:
    if c not in initials:
        print(c, end='')
print('\n')

for i, txtfile in enumerate([medical, positive]):
    print('The following are repeated in text file ' + str(i) + ':')
    for w in txtfile:
        if medical.count(w) > 1:
            print(w)
