Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuples
a=(4,6.7,8+9j,"python",True,False)
print(a)
(4, 6.7, (8+9j), 'python', True, False)
type(a)
<class 'tuple'>
a.index(8+9j)
2
len(a)
6
a.count(True)
1
#sets
#sets
#sets
a={4,7.8,"manju",5+9j,True,False}
print(a)
{False, True, (5+9j), 4, 'manju', 7.8}
type(a)
<class 'set'>
b={7,9,4,7,6,10,20,3}
print(b)
{3, 4, 20, 6, 7, 9, 10}
#methodsinset
#add
a={4,5,6,7,8,9}
a.add(15)
a
{4, 5, 6, 7, 8, 9, 15}
#issubset()
a={3,4,5,6,7,8}
b={6,7,8,9,10}
b.issubset(a)
False
a.issubset(b)
False
False
False
a={5,6,7,8,9,10,11}
b={7,8,9,10}
a.issuperset(b)
True
b.issuperset(a)
False
#union
a={3,4,5,6,7}
b={1,2,3,4,5,6,7,8}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}
#intersection
a={3,4,5,6,7}
b={1,2,3,4,7,8,9}
a.intersection(b)
{3, 4, 7}
b.intersection(a)
{3, 4, 7}
#difference
a={7,8,9,10,11,12,13}
b={8,9,10,11,12,13,14,15}
a.difference(b)
{7}
b.difference(a)
{14, 15}

#update
a={2,3,4,5,6}
b={1,4,5,6,7,8,9}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
#symmetricdifference
a={2,3,4,5,6,7,8}
b={1,4,6,8,9,10,11}
a.symmetric_difference(b)
{1, 2, 3, 5, 7, 9, 10, 11}
#differenceupdate
a={4,5,6,7,8,9}
b={1,2,3,4,5,6,10}
a.difference_update(b)
a
{7, 8, 9}
b.difference_update(a)
b
{1, 2, 3, 4, 5, 6, 10}
#intersectionupdate
a={3,4,5,6,7,8}
b={5,6,7,8,9,10}
a.intersection_update(b)
a
{8, 5, 6, 7}
b.intersection_update(a)
b
{8, 5, 6, 7}
b
{8, 5, 6, 7}
#symmetricupdate
a={11,12,13,14,15,16}
b={13,14,15,16,17,18}
a.symmetric_update(b)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.symmetric_update(b)
AttributeError: 'set' object has no attribute 'symmetric_update'
a.symmetric_difference_update(b)
a
{17, 18, 11, 12}
{17, 18, 11, 12}
{17, 18, 11, 12}
b.symmetric_difference_update(a)
b
{16, 11, 12, 13, 14, 15}
#pop
a={3,4,5,6,7,8}
a.pop()
3
a.pop()
4
a.pop(2)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a.pop(2)
TypeError: set.pop() takes no arguments (1 given)
>>> #remove
>>> a.remove(6)
>>> a
{5, 7, 8}
>>> #copy
>>> a={10,20,30,40,50}
>>> a.copy()
{50, 20, 40, 10, 30}
>>> b=a.copy()
>>> b
{50, 20, 40, 10, 30}
>>> a.discard(50)
>>> a
{20, 40, 10, 30}
>>> a.clear()
>>> a
set()
>>> set()
set()
>>> b=set()
>>> b.add(100)
>>> b
{100}
>>> a={2,3,4,5,6}
>>> b={6,7,8,9,10}
>>> a.isdisjoint(b)
False
