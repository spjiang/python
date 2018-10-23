#!/usr/bin/python
# -*- coding: UTF-8 -*-

print filter(lambda x:x and len(x.strip()) > 0 , ['test', None, '', 'str', '  ', 'END'])