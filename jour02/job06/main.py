#!/usr/local/bin/python3

for i in range(2, 1001):
    est_premier = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            est_premier = False
            break
    if est_premier:
        print(i)