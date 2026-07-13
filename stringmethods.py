Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="codegnan"
len(a)
8
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
e="i am in vja"
len(e)
11
#count()
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("k")
2
a.count("l")
4
a.count(" ")
3
b=13389
b.count(3)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    b.count(3)
AttributeError: 'int' object has no attribute 'count'
a.count("r")
1
a.count("w")
2
#find a string
a="python"
a[1]
'y'
a.find("h")
3
a.find("n")
5
b="hello"
b.find("l")
2
d[2:4]
''

a.find("k")
-1
b[2:4]
'll'
b["o"]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    b["o"]
TypeError: string indices must be integers, not 'str'
b.find["o"]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    b.find["o"]
TypeError: 'builtin_function_or_method' object is not subscriptable
TypeError: 'builtin_function_or_method' object is not subscriptable
SyntaxError: invalid syntax
b.find("o")
4
#escape sequences
#n->new line
#t->tab space (4-8)
a="name\nmailid\tmobileno\ncollege\tbranch
SyntaxError: unterminated string literal (detected at line 1)

a="name\nmailid\tmobileno\ncollege\tbranch"
a
'name\nmailid\tmobileno\ncollege\tbranch'
print(a)
name
mailid	mobileno
college	branch
b="name:Manju Harini\nmailid:manjuharinikolanti@gmail.com\tmobileno:7799281828\ncollege:VRSEC\tbranch:AI&DS"
print(b)
name:Manju Harini
mailid:manjuharinikolanti@gmail.com	mobileno:7799281828
college:VRSEC	branch:AI&DS
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="work work until you succeed"
a.replace("work","wait",1)
'wait until you succeed'
#upper
a="code"
a.upper()
'CODE'
#lower
b="hello"
b.upper()
'HELLO'
c="python"
c[0].upper
<built-in method upper of str object at 0x00007FFEF2C78BC8>
c[0].upper()
'P'
c.capitalize()
'Python'
d="i am in class"
d.title()
'I Am In Class'
d.capitalize()
'I am in class'
#isupper,islower,isalpha,isdigit
a="code"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
c="code course"
c.isalpha()
False
c="codecourse"
c.isalpha()
True
d=123
d.digit()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    d.digit()
AttributeError: 'int' object has no attribute 'digit'
d="123"
d.isalpha()
False
d.isdigit()
True
a="manju123"
a.isalnum()
True
b="manju@123"
b.isalnum()
False
#startswith
a="data science"
a.startswith("d")
True
a.endswith("e")
True
#strip
#lstrip
#rstrip
a="       manju                  "
a.strip()
'manju'
a.lstrip()
'manju                  '
a.rstrip()
'       manju'
#split
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i love python"
b.split()
['i', 'love', 'python']
#join
b="html","css","java","c"
"".join(b)
'htmlcssjavac'
" ".join(b)
'html css java c'
>>> #concatenation
>>> a="code"
>>> b="gnan"
>>> print(a+b)
codegnan
>>> a="python"
>>> b="course"
>>> print(a+" "+b)
python course
>>> f_name="manju"
>>> l_name="harini"
>>> print(f_name+l_name)
manjuharini
>>> print(f_name+" "+l_name)
manju harini
>>> print((f_name+" "+l_name).title())
Manju Harini
>>> Manju Harini
SyntaxError: invalid syntax
>>> #formatting
>>> a=5
>>> b=6
>>> print(a+b)
11
>>> print("Sum is",a+b)
Sum is 11
>>> city="vja"
>>> print("City is ",city)
City is  vja
>>> #format()
>>> a="motu"
b="pathlu"
print("hello {}{}".format(a,b))
hello motupathlu
print("hello {}  {}".format(a,b))
hello motu  pathlu
print("hello {}\n{}".format(a,b))
hello motu
pathlu
print("hello {}\nhello {}
      
SyntaxError: unterminated string literal (detected at line 1)
print("hello {}\nhello {}".format(a,b))
      
hello motu
hello pathlu
#fstring
      
a="manju"
      
b="harini"
      
print(f"hello {a}{b}")
      
hello manjuharini
