Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arithmetic
a=2
b=6
print(a+b)
8
print(a-b)
-4
print(a*b)
12
print(a**b)
64
print(a//b)
0
print(a/b)
0.3333333333333333
print(a%b)
2
#assignment
a=3
b=5
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
8
a-=3
a
5
a*=2
a
10
a**=4
a
10000
a//=2
a
5000
a/=2
a
2500.0
a%=2
a
0.0
b+=a
b
5.0
b-=3
b
2.0
b*=2
b
4.0
b**=3
b
64.0
b//=2
b
32.0
b/=4
b
8.0
b%=3
b
2.0
#comparision
a=6
b=8
a<b
True
b>a
True
a<=b
True
b>=a
True
a>b
False
b<a
False
a!=b
True
a==b
False
a=b
a=b
a=6
b=6
a==b
True
#Logical
a=4
b=8
a<b and b>a
True
a<=b and b>=a
True
a!=b or a==b
True
a!=b or a==b
True
not True
False
not False
True
#identify operators
#identify operators
a=6
type(a) is int
True
type(a) is not int
False
b=2.3
type(b) is int
False
type(b) is not int
True
type(b) is float
True
type(b) is not float
False
c="code"
type(c) is string
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    type(c) is string
NameError: name 'string' is not defined. Did you forget to import 'string'?
type(c) is str
True
type(c) is not str
False
d=3+5j
type(d) is complex
True
type(d) is not complex
False
e=True
type(e) is bool
True
type(e) is not bool
False
#membership
a=2,3,4,5,6,7,8,9
9 in a
True
9 not in a
False
10 not in a
True
10 in a
False
#bitwise
#bitwise
a=2
b=4
a&b
0
bin(2)
'0b10'
bin(4)
'0b100'
a=7
b=9
bin(7)
'0b111'
bin(9)
'0b1001'
a=3
b=8
bin(3)
'0b11'
bin(8)
'0b1000'
a&b
0
a=3
b=8
>>> a|b
11
>>> a=2
>>> b=6
>>> b=6
>>> a=6
>>> -(a+1)
-7
>>> ~a
-7
>>> b=-12
>>> ~b
11
>>> c=-6
>>> ~c
5
>>> d=4
>>> -(d+1)
-5
>>> a=5
>>> b=7
>>> a^b
2
>>> bin(a)
'0b101'
>>> bin(b)
'0b111'
>>> a=8
>>> b=10
>>> a^b
2
