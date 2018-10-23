#!/usr/bin/python
# -*- coding: UTF-8 -*-
def get_y(a,b):
    def func():
        return a+b
    return func
y1 = get_y(1,1)

print y1()