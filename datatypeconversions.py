Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype conversions
#int
int(4)
4
int(8.2)
8
int("hi") #string cannot be converted into integer
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("hi") #string cannot be converted into integer
ValueError: invalid literal for int() with base 10: 'hi'
int(5+9j) #complex values cannot be converted into integer
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(5+9j) #complex values cannot be converted into integer
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(4)
4.0
float(5.6)
5.6
float("hello") #string cannot be converted into float
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("hello") #string cannot be converted into float
ValueError: could not convert string to float: 'hello'
float(6+3j) #complex cannot be converted into float
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(6+3j) #complex cannot be converted into float
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#str
str(5)
'5'
str(7.8)
'7.8'
str("python")
'python'
str(6+9j)
'(6+9j)'
str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(4)
(4+0j)
>>> complex(4.2)
(4.2+0j)
>>> complex("manju")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    complex("manju")
ValueError: complex() arg is a malformed string
>>> complex(6+9j)
(6+9j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #bool
>>> bool(8)
True
>>> bool(8.9)
True
>>> bool("hello")
True
>>> bool(5+9j)
True
>>> bool(True)
True
>>> bool(False)
False
