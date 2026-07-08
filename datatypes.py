Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=5
type(a)
<class 'int'>
b=7.8
type(b)
<class 'float'>
c='code'
type(c)
<class 'str'>
d="code"
type(d)
<class 'str'>
e='''code'''
type(e)
<class 'str'>
>>> x=5+3j
>>> type(x)
<class 'complex'>
>>> x= 4+2i  #imaginary value should only be j
SyntaxError: invalid decimal literal
>>> z=6j
>>> type(z)
<class 'complex'>
>>> y=3j+7
>>> type(y)
<class 'complex'>
>>> f="c"
>>> type(f)
<class 'str'>
>>> g=True
>>> type(g)
<class 'bool'>
>>> h=true #t should always be capital letter
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    h=true #t should always be capital letter
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> c=False
>>> type(c)
<class 'bool'>
>>> g=false #f should always be capital
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    g=false #f should always be capital
NameError: name 'false' is not defined. Did you mean: 'False'?
