#!/usr/bin/python
# -*- coding: UTF-8 -*-
count = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (i != j) and (j != k):
                print i, j, k
                count += 1

print count