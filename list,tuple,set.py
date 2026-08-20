Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list
a=[2,3.4,"python",7+9j,True,False]
a
[2, 3.4, 'python', (7+9j), True, False]
type(a)
<class 'list'>
b=8.9
type(b)
<class 'float'>
c=[8.9]
type(c)
<class 'list'>
#methods
#append-used to add one value in list
a=["python","java","c","c++"]
a.append("ml")
a
['python', 'java', 'c', 'c++', 'ml']
a.append("ai","ds")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.append("ai","ds")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ds","ai"])
a
['python', 'java', 'c', 'c++', 'ml', ['ds', 'ai']]
#we cannot add more in append method to add more we have to use extend
#extend-to add more values in the list
a=["vija","hyd"]
a.extend(["chennai","vzg"])
a
['vija', 'hyd', 'chennai', 'vzg']
#insert -to add value in particular position
b=["black","blue","red"]
b.insert(1,"white")
b
['black', 'white', 'blue', 'red']
#index-gives the index value of our input
a=["hi","hello","how"]
a.index("how")
2
#copy-copies the value like to add same data in other varaible also
a.copy()
['hi', 'hello', 'how']
b=a.copy()
b
['hi', 'hello', 'how']
#clear-clears the data in the list
b.clear()
b
[]
a.clear()
a
[]
#sort
#sort-order
a=["apple","grapes","mango","pineapple"]
a.sort()
a
['apple', 'grapes', 'mango', 'pineapple']
b=[8,3,5,9,2,4]
b.sort()
b
[2, 3, 4, 5, 8, 9]
#reverse-prints from last value
a=["java","python","ml","ai","ds"]
a.reverse()
a
['ds', 'ai', 'ml', 'python', 'java']
b=[9,2,3,1,4,6]
b.reverse()
b
[6, 4, 1, 3, 2, 9]
#pop-deletes the last value if no index given in brackets if value is given in brackets that positioned value will be deleted.
a=["sweety","cuty","smarty","hearty"]
a.pop()
'hearty'
a
['sweety', 'cuty', 'smarty']
a.pop(0)
'sweety'
a
['cuty', 'smarty']
a.pop("cuty")
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.pop("cuty")
TypeError: 'str' object cannot be interpreted as an integer
#we cannot delete by giving value in pop so we use remove
#remove
a.remove("cuty")
a
['smarty']
#length
a=["biryani","choclates","icecream"]
len(a)
3
b="choclates"
len(b)
9
c=["choclates"]
len(c)
1
a.count("icecream")
1
#TUPLE
#TUPLE()
a=(4,6.8,"hi",3+4j,True,False)
print(a)
(4, 6.8, 'hi', (3+4j), True, False)
type(a)
<class 'tuple'>
#methods-count,index #tuple is immutable
len(a)
6
a.count(True)
1
a.index("hi")
2
#SET
#SET{}-set is a unordered,semi mutable,do not allow duplicates
a={5,8.3,"manju",4+6j,True,False}
print(a)
{False, True, 'manju', 5, (4+6j), 8.3}
type(a)
<class 'set'>
b={3,6,5,8,3,8,1,3,2}
print(b)
{1, 2, 3, 5, 6, 8}
#methods
#subset
a={4,5,6,7,8,9,10}
b={7,8,9,10}
a.issubset(b)
False
b.issubset(a)
True
#superset
a.issuperset(b)
True
b.issuperset(a)
False
#union-merging the sets and remove duplicates
a={8,9,10,11,12,13}
b={11,12,13,14,15,16}
a.union(b)
{8, 9, 10, 11, 12, 13, 14, 15, 16}
b.union(a)
{8, 9, 10, 11, 12, 13, 14, 15, 16}
#intersection
a={4,5,6,7,8,9}
b={7,8,9,10,11,12}
a.intersection(b)
{8, 9, 7}
b.intersection(a)
{8, 9, 7}
#update-forms new set after combining
a={3,4,5,6,7}
b={4,5,6,7,8,9}
a.update(b)
a
{3, 4, 5, 6, 7, 8, 9}
b.update(a)
b
{3, 4, 5, 6, 7, 8, 9}
#difference-prints which are different
a=[6,7,8,9,10,11,12]
b=
SyntaxError: invalid syntax
a={6,7,8,9,10,11,12}
b={9,10,11,12,13}
a.difference(b)
{8, 6, 7}
b.difference(a)
{13}
#symmetric difference-deletes same ones and prints by merging both inputs
a={10,20,30,40,50}
b={40,50,60,70,80}
a.symmetricdifference(b)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    a.symmetricdifference(b)
AttributeError: 'set' object has no attribute 'symmetricdifference'. Did you mean: 'symmetric_difference'?
a.symmetric_difference(b)

{80, 20, 70, 10, 60, 30}
#difference_update
#deletes common ones and updates as new one
a={1,2,3,4,5,6}
b={4,5,6,7,8,9}
a.difference_update(b)
a
{1, 2, 3}
b.difference(a)
{4, 5, 6, 7, 8, 9}
b.difference_update(a)
b
{4, 5, 6, 7, 8, 9}
#intersection_update
a={3,4,5,6,7,8}
b={1,2,3,4,5,6}
a.intersection_update(b)
a
{3, 4, 5, 6}
b.intersection_update(a)
b
{3, 4, 5, 6}
#symmetricdifferenceupdate
a={7,8,9,10,11,12,13}
b={10,11,12,13,14,15}
a.symmetric_difference_update(b)
a
{7, 8, 9, 14, 15}
b.symmetric_difference_update(a)
b
{7, 8, 9, 10, 11, 12, 13}
#pop-picks first one to delete and cannot take position number
a={5,6,7,8,9}
a.pop()
5
a.pop(1)
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    a.pop(1)
TypeError: set.pop() takes no arguments (1 given)
a.pop(9)
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    a.pop(9)
TypeError: set.pop() takes no arguments (1 given)
#to delete particular element we have to use remove
a.remove(1)
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    a.remove(1)
KeyError: 1
a.remove(9)
a
{6, 7, 8}
#copy
a={7,8,9,10}
a.copy()
{8, 9, 10, 7}
b=a.copy()
b
{8, 9, 10, 7}
#clear
a.clear()
a
set()
#add
b=set()
b.add(2)
b
{2}
c=[]
>>> c.extend("manju")
>>> c
['m', 'a', 'n', 'j', 'u']
>>> a={6,7,8,9}
>>> len(a)
4
>>> #set does not have count and index beacause set do not follow particular order and no duplicate values
>>> a.count(8)
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    a.count(8)
AttributeError: 'set' object has no attribute 'count'
>>> a.index(6)
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    a.index(6)
AttributeError: 'set' object has no attribute 'index'
>>> #disjoint-different should be there otherwise it will print false
>>> a={5,6,7,8}
>>> b={8,9,10,11}
>>> a.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
>>> a.isdisjoint(b)
False
>>> a={1,2,3,4}
>>> b={5,6,7,8}
>>> a.isdisjoint(b)
True
