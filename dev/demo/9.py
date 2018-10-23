#!/usr/bin/python
# -*- coding: UTF-8 -*-
def f1(x):
    return x*2

def new_fn(f):
    def fn(x):
        print "call "+f.__name__+"()"
        return f(x)
    return fn
