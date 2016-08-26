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

for i, c in enumerate(trial_name):
    selected = select_starts_with(c, medical)
    if i == 0:
        print(choice(selected).capitalize(), end=' ')
    elif i == len(trial_name) - 1:
        print(choice(selected), end='.\n')
    else:
        print(choice(selected), end=' ')
