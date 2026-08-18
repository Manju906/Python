Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="hello"
len(a)
5
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count()
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("t")
5
a.count("l")
4
a.count(" ")
3
a.count("a")
1
len(a)
27
#find a string (opposite of indexing)
a="python"
a[2]
't'
a.find("t")
2
a.fiind("p")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.fiind("p")
AttributeError: 'str' object has no attribute 'fiind'. Did you mean: 'find'?
a.find("p")
0
b="hello"
b.find("l")
2
b[2:4]
'll'
#escape sequences
#\n-new line
#\t-tab space(4-8)
a="name\nmobileno\temailid\ncity"
print(a)
name
mobileno	emailid
city
b="name:manju\nmobile no:91092839103\temailid:manjuharinikolanti@gmail.com\ncity:vijayawada"
print(b)
name:manju
mobile no:91092839103	emailid:manjuharinikolanti@gmail.com
city:vijayawada
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="india pakisthan"
b.replace("pakisthan","austrailia")
'india austrailia'
c="wait wait until you succeed"
c.replace("wait","work")
'work work until you succeed'
c.replace("wait","work",1)
'work wait until you succeed'
#upper
a="hello"
a.upper() #in upper brackets should always be empty
'HELLO'
b="HI"
b.lower()
'hi'
a="python"
a.upper(0)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.upper(0)
TypeError: str.upper() takes no arguments (1 given)
a[0].upper()
'P'
#To over come this we use capitalize to make starting letter capital
#capitalize
a="python course"
a.capitalize()
'Python course'
b="codegnan it solutions"
b.capitalize()
'Codegnan it solutions'
c="i am in class"
c.capitalize()
'I am in class'
#To make every starting letter capital in a sentence we use title()
#Title
a="i am in class"
a.title()
'I Am In Class'
b="codegnan it solutions"
b.title()
'Codegnan It Solutions'
c=i love python"
SyntaxError: unterminated string literal (detected at line 1)
c="i love python"
c.title()
'I Love Python'
#conditions in string methods
a="data"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
b="data science"
b.isalpha()
False
b="datascience"
b.isalpha()
True
c="java"
c.isalnum()
True
>>> #in isalnum any one like alpha can include or num can include or both can include
>>> d="java123"
>>> d.isalnum()
True
>>> #we cannot give digits seperately
>>> a=56789
>>> a.isdigit()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
>>> a="56789"
>>> a.isdigit()
True
>>> a="hello world"
>>> a.startswith("h")
True
>>> a.endswith("d")
True
>>> a.endswith("e")
False
>>> #concatenation
>>> a="python"
>>> b="course"
>>> print(a+b)
pythoncourse
>>> a="hello"
>>> b="world"
>>> print(a+b)
helloworld
>>> fname="manju"
>>> lname="harini"
print(fname+lname)
manjuharini
print(fname+" "+lname)
manju harini
print(fname.title()+" "+lname.title())
Manju Harini
print((fname+" "+lname).title())
Manju Harini
#strip
#lstrip(),rstrip()
a="                   manju                   "
a.strip()
'manju'
a.lstrip()
'manju                   '
a.rstrip()
'                   manju'
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="I am learning python fullstack"
b.split()
['I', 'am', 'learning', 'python', 'fullstack']
#join
#join()
a="vja","hyd","vzg"
"".join(a)
'vjahydvzg'
" ".join(a)
'vja hyd vzg'
"bng".join(a)
'vjabnghydbngvzg'
#formatting -adding additional data
a=4
b=7
print(a+b)
11
print("the sum is ",a+b)
the sum is  11
city="vjy"
print("the city is",city)
the city is vjy
#format method
a="motu"
b="pathlu"
print("hello {}{}".format(a,b))
hello motupathlu
print("hello {} {}".format(a,b))
hello motu pathlu
print("hello {} hello {}".format(a,b))
hello motu hello pathlu
print("hello {}\n hello {}".format(a,b))
hello motu
 hello pathlu
print("hello {}\nhello{}".format(a,b))
hello motu
hellopathlu
print("hello {}\nhello {}".format(a,b))
hello motu
hello pathlu
#fstring
a="manju"
b="harini"
print(f"hello {a}{b}")
hello manjuharini
print(f"hello {a} hello {b}")
hello manju hello harini
print(f"hello {a}\n hello {b}")
hello manju
 hello harini
print(f"hello {a}\nhello {b}")
hello manju
hello harini
