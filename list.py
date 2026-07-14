Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,4.5,"python",6+9j,True,False]
print(a)
[2, 4.5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=8.9
type(b)
<class 'float'>
b=[8.9]
type(b)
<class 'list'>
c=[8.9]
type(c)
<class 'list'>
#methods
#append
a=["python","c","c++","java"]
a
['python', 'c', 'c++', 'java']
a.append("html","css")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.append("html","css")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["html","css"])
a
['python', 'c', 'c++', 'java', ['html', 'css']]
#extend
a=["html","css","js"]
a.extend(["python","java"])
a
['html', 'css', 'js', 'python', 'java']
#insert
b=["vja","hyd","vzg"]
b.insert(1,"chennai")
b
['vja', 'chennai', 'hyd', 'vzg']
#index
a=["apple","banana","grapes"]
a.index("grapes
        
SyntaxError: unterminated string literal (detected at line 1)
a.index("grapes")
        
2
a.copy()
        
['apple', 'banana', 'grapes']
b=a.copy()
        
b
        
['apple', 'banana', 'grapes']
a.count("apple")
        
1
len(a)
        
3
d="apple"
        
len(d)
        
5
e=["apple"]
        
len(e)
        
1

#sort
        
a=["mango","kiwi","dragon"]
        
a.sort()
        
a
        
['dragon', 'kiwi', 'mango']
a=["ds","ai","ml"]
        
a.reverse()
        
a
        
['ml', 'ai', 'ds']
b=[2,4,5,8,9]
        
b.reverse()
        
b
        
[9, 8, 5, 4, 2]

#pop()
        
a=["black","white","red","blue","pink"]
        
a.pop()
        
'pink'
a
        
['black', 'white', 'red', 'blue']
a.pop(2)
        
'red'
a
        
['black', 'white', 'blue']
a.pop
        
<built-in method pop of list object at 0x000001EF72AB7700>





>>> a.pop("black")
...         
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.pop("black")
TypeError: 'str' object cannot be interpreted as an integer
>>> a.remove("black")
...         
>>> a
...         
['white', 'blue']
>>> ['white', 'blue']
...         
['white', 'blue']
>>> 
>>> a=["ap","ts","ka"]
...         
>>> a.clear()
...         
>>> a
...         
[]
>>> b=[]
...         
>>> b.append("manju")
...         
>>> b
...         
['manju']
>>> a=[10,20,30,40,"code"]
...         
