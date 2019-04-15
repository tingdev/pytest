# %%
import argparse
import sys
import copy
import math
import os

import matplotlib.pyplot as plt
import numpy as np
import ptvsd
import pprint
import pyperclip
import re

'''
Below is for local attach debugging

# 5678 is the default attach port in the VS Code debug configurations
print("Waiting for debugger attach")
ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
ptvsd.wait_for_attach()
breakpoint()
'''

# try input args
print("argv " + str(sys.argv))
parser = argparse.ArgumentParser({})
parser.add_argument('--name', help='person name', default=None, type=str)
parser.add_argument('--age', help='person age', default=20, type=int)
if (len(sys.argv)==1):
    parser.print_help()
    #sys.exit(1)
ns =parser.parse_args()
print(ns)

# %%
msg = 'a simple cell'
print(msg)
# %%

try:
    int('99.99')
except BaseException:
    print('oops1!')

try:
    print(str(int(float('99.99'))))
except BaseException:
    print('oops2!')


def DBG(topic, content):
    print(topic + ':' + str(content))


def add(left, right):
    return left + right


print(add(100, 200))
print(math.log10(3))

try:
    s = 10 / 0
except BaseException:
    print('exception!!!')

DBG('operators', [11 / 3, 11 // 3, 11 %
                  3, 11**3, 1 > 3 and 3 > 1, 1 > 3 or 3 > 1])

eggs = 1


def testEggs():
    eggs = 3
    print('eggs is' + str(eggs))


testEggs()

for i in range(10, 20, 2):
    print('i is' + str(i))

# try reference


def tryRefModifyFirst(mutable, newValue):
    mutable[0] = newValue


# mutable list
lst = [1, 2, 3]
DBG('lst', lst)
lst.append(4)
DBG('lst appended', lst)
lst.sort(reverse=True)
DBG('lst reverse', lst)

# anotherlst is also a REFERENCE points to the same content as the lst!
anotherlst = lst
DBG('anotherlist', anotherlst)
anotherlst[0] = 0
DBG('anotherlist modifed', anotherlst)

# REFERENCE to func!
tryRefModifyFirst(lst, 55)
DBG('after call func with ref', lst)

# embeded a list in lst
lst[2] = [44, 55, 66]
DBG('lst with lst', lst)

# if I copy it
copylst = copy.copy(lst)
DBG('the copy lst', copylst)
tryRefModifyFirst(copylst, 33)
DBG('the copy lst after modified', copylst)
DBG('orig lst remain untouched!', lst)

# however if I modified the inside list, the original lst would also be changed
copylst[2][0] = 33333
DBG('modified the inside lst of the copy lst', copylst)
DBG('wow! the inside lst of the original lst is also changed!', lst)

# so we need a deep copy
deepCopylst = copy.deepcopy(lst)
DBG('the deep copy lst', deepCopylst)
tryRefModifyFirst(deepCopylst, 33)
DBG('the copy lst after modified', deepCopylst)
DBG('orig lst remain untouched!', lst)
deepCopylst[2][0] = 88888
DBG('modified the inside lst of the deep copy lst', deepCopylst)
DBG('the inside lst of the original lst remain untouched', lst)

# iterator
for i in lst:
    print('i is' + str(i))

# immutable tuple!
tuple = (1, 2, 3)
DBG('tuple orig', tuple)
try:
    tuple[0] = 3        # intentionally! 
except BaseException:
    DBG('tuple set', 'oops! tuple is immutalbe! exception!')

anotherTuple = tuple
DBG('another tuple is a copy of orig tuple, since it\'s immutable', anotherTuple)

tolist = list(tuple)
tolist[0] = 33
DBG('tuple to list and modified', tolist)

# funny tuple
justAnInt = (22)
DBG('just an int', justAnInt)
funTuple = (22,)
DBG('funny tuple', funTuple[0])

# for fun
DBG('is None?', tuple is None)

# dict and str operation
houses = {'tianyu': 4*133, 'tianxi': 4*90,
          'baolong': 3.5*33, 'lanshan': 1.3*120, 'jiayuan': 75}
pprint.pprint(houses)  # pretty print
result = {}             # empty dict
result['totalnum'] = len(houses.items())
for n, p in houses.items():
    # don't worry! set default won't set the value of the key to 0 each time.
    result.setdefault('totalprice', 0)
    result['totalprice'] += p

DBG('total real estate num'.ljust(25, '-'), result['totalnum'])
DBG('total real estate price'.ljust(25, '-'), result['totalprice'])

# try clipboard!
clip = pyperclip.paste()
rev = ''
for i in clip:
    rev = i + rev
DBG('reverse the string from clip! ', rev)

# str operation
DBG('in or not in', 'hello' in 'helloworld')
DBG('not in',  'yes' not in 'yes')

stri = '  you\'re the best, man!  '
DBG(':', stri[:5])
DBG(':', stri[1:])
DBG(':', stri[1:5])

DBG('upper' , stri.upper())
DBG('is lower' , stri.islower())
DBG('startwith', stri.startswith('you'))
DBG('split', stri.split('e'))       # default separator is ' '
DBG('strip', stri.strip())
DBG('lstrip', stri.lstrip())
DBG('rstrip', stri.rstrip())
DBG('strip with optional chars', stri.strip(' ye!'))

DBG('is decimal', '134'.isdecimal())

# plot fun
#x = np.linspace(0, 20, 100)
#plt.plot(x, np.sin(x))
#plt.plot(x, np.cos(x))
#plt.show()

po = re.compile(r'''
    ^S\d{3}
    @
    (tianyu|tianxi|baolong|lanshan|wsjy)
    (opt.)?
    (s*)(k)*
    (C){2}
    (tx){3,5}?
    ''', re.VERBOSE)
mo = po.search('S234@tianyussskkkCCtxtxtxtx')
if (mo != None):
    DBG('search', str(mo.group()))
    DBG('search', str(mo.group(1)))
    DBG('search', str(mo.group(2)))
    DBG('search', str(mo.group(3)))       # sss
    DBG('search', str(mo.group(4)))       # k
    DBG('search', str(mo.group(5)))       # C
    DBG('search', str(mo.group(6)))       # tx
else:
    DBG('regex', 'not find!')

po = re.compile(r'(\d{3})-(\d{2})')
lo = po.findall('123-456 and 889-27 and 281-321')
if (lo != None):
    DBG('findall', str(lo))

po = re.compile(".*", re.DOTALL)
str2op = 'hi\nman\nyou\'re great!'
lo = po.findall(str2op)
if (lo != None):
    DBG('compile with arg', str(len(lo)) + str(lo))     # NOTE! because '.*' also matches '', so there's an empty str in the result list!

lo = po.search(str2op)
if (lo != None):
    DBG('search', lo.group())

mo = re.match("(?P<key1>.*)\n(?P<key2>.*)\n", str2op)   # (?P<k>v) group matched will be in the dict {k:v}
if (mo != None):
    DBG('match', mo.groupdict())

subpattern = re.compile(r'(Stupid|Mad|Sucks) (\w)\w*', re.IGNORECASE)
newstr = subpattern.sub(r'\2***', 'Stupid man, how mad you are, sucks ho!') # matched will be replaced with group2***
DBG('sub', newstr)

DBG('findall', re.findall(r'(\dasd)', '1asd2asdp4asdsas'))
DBG('findall', re.findall(r'(\dasd)+', '1asd2asdp4asdsas'))
DBG('findall', re.findall(r'(\dasd)*', '1asd2asdp4asdsas'))     # NOTICE the last result empty ''

print('end')

