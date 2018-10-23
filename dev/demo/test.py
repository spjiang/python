#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
'''
class Employee:
    pass

john = Employee() # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
# print john.name, john.dept
'''

'''
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print "B"
    except C:
        print "C"
    except D:
        print "D"
'''

'''
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
iter(rev)
for char in rev:
    print(char)
'''

'''
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print char
'''

'''
yvec = [7, 5]
xvec = [10]
print sum(x * y for x, y in zip(xvec, yvec))
'''

'''
from math import pi, sin
sine_table = {x: sin(x * pi / 180) for x in range(0, 91)}

print sine_table
'''

'''
unique_words = set(word for line in page for word in line.split())
'''

'''
import os
print os.getcwd()
os.chdir('../')
print os.system('mkdir today')
'''

'''
import os
#print dir(os)
print help(os)
'''

'''
import shutil
shutil.copyfile('test.py', 'test2.py')
shutil.move('./test2.py', '../test2.py')
'''

'''
import glob
print glob.glob('*.py')
'''

'''
import sys
#python test.py one two three
print sys.argv
'''

'''
import re

#print re.findall(r'\bab[a-z]*', 'abcsdsadas abc asdsadasdabcasdsa')

print re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

'''

'''
print 'tea for too'.replace('too', 'two')
'''

'''
print xrange(100)
'''

'''
import urllib2
for line in urllib2.urlopen('http://www.baidu.com'):
    line = line.decode('utf-8')
    if 'common' in line or 'DET' in line:
        print line
'''

'''
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('452985064@qq.com', 'spjiang@aliyun.com', 'test')
server.quit
'''

'''
from datetime import date
now = date.today()
print now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

birthday = date(1988, 2, 12)
age = now - birthday
print age
print age.days/365
'''

'''
import zlib
s = b'witch which has which witches wrist watch'
print len(s)

t = zlib.compress(s)
print len(t)

r = zlib.decompress(t)
print r

print zlib.crc32(s)
'''

'''
from timeit import Timer
print Timer('t=a;a=b;b=t', 'a=1;b=2').timeit()
print Timer('a,b = b,a', 'a=1; b=2').timeit()
'''

'''
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print average([20, 30, 70])
    40.0
    """
    return sum(values, 0.0) / len(values)


import unittest
class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError,average,[])
        self.assertRaises(TypeError, average, 20, 30, 70)

unittest.main()
'''

'''
import repr
repr.repr(set('supercalifragilisticexpialidocious'))

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width = 30)

import textwrap
doc = """The wrap() method is just like fill() except that it returns
    a list of strings instead of one big string with newlines to separate
    the wrapped lines. """
print textwrap.fill(doc, width = 70)
'''

'''
import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
conv = locale.localeconv()
x = 1234567.8
print locale.format("%d", x, grouping = True)
print locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping = True)
'''

'''
from string import Template
t = Template('${village}folk send $$10 to $cause.')
#print t.substitute(village = 'Nottingham', cause = 'the ditch fund')

t = Template('Return the $item to $owner.')
d = dict(item = 'unladen swallow')
print t.safe_substitute(d)
'''

'''
import time, os.path
from string import Template
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format):    ')

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))
'''
#print 'ABC'.encode('ascii')
#print '中文'.encode('utf-8')

'''
class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1

A = Student('A')
B = Student('B')
C = Student('C')
D = Student('D')

print Student.count
'''

'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

for n in Fib():
     print(n)

'''


'''
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
            print a, '===', b
        return b

f = Fib()

print f[5]
'''
'''
print list(range(10))[5:10]
print range(10)[5:10]
'''

'''
class Chain(object):

    def __init__(self, path=''):
        print 'a'
        print 'path:'+path
        self._path = path
        print 'path2:'+path

    def __getattr__(self, path):
        print 'b'
        print 'path3:'+path
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        print 'c'
        print 'path4:'+self._path
        return self._path

    __repr__ = __str__


print Chain().status.user.timeline.list
'''

'''
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Michael')
print s()
'''
'''
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
'''

'''
from enum import Enum, unique
import sys


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print day1
sys.exit()
'''

'''
from enum import Enum, unique
@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student():
    def init(self, name, gender):
        self.name = name
        if isinstance(gender, Gender):
            self.gender = gender
        else:
            raise ValueError('只允许接收Gender类型的参数')


sex = Gender.Male.value

bart = Student('Bart', sex)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
'''
'''
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
'''

'''
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n
foo(0)
'''
'''
import logging
logging.basicConfig(level = logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
'''

'''
import pdb
s = '0'
n = int(s)
pdb.set_trace()  # 运行到这里会自动暂停
print(10 / n)
'''
'''
with open('./workfile', 'r') as f:
    for line in f.readlines():
        print(line.strip())  # 把末尾的'\n'删掉
'''

'''
import os
#print os.environ.get('PATH')
#print os.environ.get('x', 'default')

print os.path.abspath('.')

print [x for x in os.listdir('.') if os.path.isdir(x)]
'''

'''
from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s) ...' % (name, os.getpid()))
    
if __name__ == '__main__':
    print('Parent process %s.' % os.getppid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
'''
'''
from multiprocessing import Pool
import os, time, random
def long_time_task(name):
    print('Run task %s (%s) ...' % (name, os.getpid()))
    start = time.time()
    print start
    print random.random()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds ' % (name, (end - start)))
if (__name__ == '__main__'):
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocessing done...')
    p.close()
    p.join()
    print('All subprocessing done.')
'''

'''
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.com'])
print 'Exit code:', r
'''

'''
import socket
import threading
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.baidu.com', 80))
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

with open('baidu.html', 'wb') as f:
    f.write(html)

'''

import socket
import threading
import time


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            print '11'
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
        sock.close()
        print('Connection from %s:%s closed.' % addr)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')
while True:
    print '1'
    sock, addr = s.accept()
    print '2'
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


    

























    





 
































