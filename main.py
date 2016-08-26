#!/usr/bin/env python3
from random import choice

medical = open('medical.txt', 'r').read().splitlines()
positive = open('positive.txt', 'r').read().splitlines()
trial_name = choice(positive)

def select_starts_with(letter, terms):
    selected = []
    for t in terms:
        if t[0] == letter:
            selected.append(t)
    return selected

print('Introducing the ' + trial_name.upper() + ' trial:', end=' ')

for c in trial_name:
    selected = select_starts_with(c, medical)
    print(choice(selected), end=' ')
print("\n")
