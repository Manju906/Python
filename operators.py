Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators-Arithmetic(+,-,*,//,/,%),assignment(+=,-=,*=,//=/=,%=),assignment(+=,-=,*=,//=/=,%=),comparision(>,<,<=,>=,!=,==),logical(and,or,not),identity(is,is not),membership(in,not in),bitwise(&,^,~,<<,>>)
#//-integer division or floor division
#ARITHMETIC
a=4
b=6
print(a+b)
10
print(a-b)
-2
print(a*b)
24
print(a//b)
0
print(a/b)
0.6666666666666666
print(a%b)
4
print(a**b)
4096
#ASSIGNMENT
a=2
b=5
a+=b
a
7
a-=1
a
6

a*=3
a
18
a//=2
a
9
a/=3
a
3.0
a%=2
a
1.0
a**=2
a
1.0
b+=a
b
6.0
b-=1
b
5.0
b*=3
b
15.0
b//=3
b
5.0
b/=2
b
2.5
b**=2
b
6.25
#COMPARISION
a=3
b=9
a<b
True
a>b
False
b<a
False
b>a
True
a!=b
True
a==b
False
a<=b
True
b>=a
True
b==a
False
b!=a
True
a>=b
False
b<=a
False
#LOGICAL
a=5
b=9
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a=9
b=12
a<b or b>a
True
a<=b or b>=a
True
a!=b or a==b
True
#IDENTIFY
a=3
type(a) is int
True
type(a) is not int
False
a=8.9
type(a) is float
True
type(a) is int
False
type(a) is not float
False
#MEMBERSHIP
a=3,4,5,6,7,8,9
9 in a
True
10 in a
False
10 not in a
True
>>> #BITWISE
>>> a=3
>>> b=6
>>> a&b
2
>>> a=4
>>> b=7
>>> a&b
4
>>> a=6
>>> b=7
>>> a|b
7
>>> a=4
>>> b=5
>>> a|b
5
>>> a=8
>>> b=9
>>> a^b
1
>>> a=3
>>> b=7
>>> a^b
4
>>> a=4
>>> a>>2
1
>>> b=4
>>> b<<3
32
