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
    tuple[0] = 3
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

# plot fun
x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()

print('end')