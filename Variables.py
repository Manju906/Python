Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
print(6+8)
14
a=4
b=9
print(a+b)
13
c=30
print(30)
30
z=40
print(Z)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(Z)
NameError: name 'Z' is not defined. Did you mean: 'z'?
#python is case sensitive so give same in print as the variable name
x=50
print(50)
50
name="manju"
print(name)
manju
print("name")
name
#give the var name in print statement
city="vijayawada"
print(city)
vijayawada
country="india"
print(country)
india
2=30
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
#donot start  var name with number
a2=30
print(a2)
30
4a=10
SyntaxError: invalid decimal literal
#cannot start with number
a0123456789=100
print(a0123456789)
100
#start with letter and can contain numbers
@=50
SyntaxError: invalid syntax
#cannot start with spl characters
$=70
SyntaxError: invalid syntax
#only underscore is spl char used
_d=20
print(_d)
20
f=90
f=40
 f=35
 
SyntaxError: unexpected indent
#cannot use space before var name
#cannot use keywords
for=20
SyntaxError: invalid syntax
first name="manju"
SyntaxError: invalid syntax
#cannot give space in between
first_name="manju"
print(first_name)
manju
firstname="manju"
print(firstname)
manju
a=4,b=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> #cannot assign like this
>>> #to assign multiple values
>>> a=4;b=7
>>> print(a+b)
11
>>> #also
>>> a=5,b=6
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> #also
>>> a,b=4,5
>>> print(a+b)
9
>>> #but cannot use evrytime
>>> a=2,3,4,5,6,7,8,9
>>> print(a)
(2, 3, 4, 5, 6, 7, 8, 9)
>>> a,b,c=2,3,4
>>> print(a,b,c)
2 3 4
>>> a,b,c=2,3,4,5,6,7,8,9
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a,b,c=2,3,4,5,6,7,8,9
ValueError: too many values to unpack (expected 3, got 8)
>>> #give only according to the variables mentioned dont give more than that
>>> #unpacking
>>> a,b,c=(6,7,8)
>>> print(a,b,c)
6 7 8
>>> a=6
>>> print(a)
6
del a
print(a)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a2'?
#cannot print bcz the val has already deleted
#concatenation
fname="manju"
lname="harini"
print(fname+lname)
manjuharini
print(fname+" "+lname)
manju harini
print(fname+" "+lname) #to give space
manju harini
print(fname,lname)
manju harini
#case sensitive
name="manju"
print(Name)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    print(Name)
NameError: name 'Name' is not defined. Did you mean: 'name'?
print(NAME)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    print(NAME)
NameError: name 'NAME' is not defined
print(name)
manju
NAME="manju"
print(NAME)
manju
Name="manju"
print(Name)
manju
