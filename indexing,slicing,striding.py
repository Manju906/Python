Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="i am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[2]+a[3]
'am'
a[5]+a[6]
'in'
a[1]
' '
a[1]+a[4]+a[7]
'   '
a[1]+a[4]
'  '
b="I am learning Python
SyntaxError: unterminated string literal (detected at line 1)


b="I am Learning Python"
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
IndexError: string index out of range
b="I am Learning Python"
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
IndexError: string index out of range
c="I love codegnan"
c[7]+c[8]+c[9]+c[10]
'code'
c[2]+c[3]+c[4]+c[5]
'love'
c[11]+c[12]+c[13]+c[14]
'gnan'
b="I am Learning Python"
b[14]+b[15]+b[16]+b[17]+b[18]+b[19]
'Python'
d="vijayawada is a royal city"
d[-10]+d[-9]+d[-8]+d[-7]+d[-6]
'royal'
d[-4]+d[-3]+d[-2]+d[-1]
'city'
d[-15]+d[-14]
'is'
e="vizag is city of destiny"
e[-7]+e[-6]+e[-5]+e[-4]+e[-3]+e[-2]+e[-1]
'destiny'
e[-15]+e[-14]+e[-13]+e[-12]
'city'
e[-26]+e[-25]+e[-24]+e[-23]+e[-22]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    e[-26]+e[-25]+e[-24]+e[-23]+e[-22]
IndexError: string index out of range
#slicing
a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a="work until you succeed"
a[:4]
'work'
a[4:10]
' until'
a[5:10]
'until'
>>> a[11:14]
'you'
>>> a[15:]
'succeed'
>>> b="Time is very precious"
>>> b[13:]
'precious'
>>> b[8:12]
'very'
>>> b[0:4]
'Time'
>>> c="simple is better than complex"
>>> c[-19:-13]
'better'
>>> c[-29:-23]
'simple'
>>> c[-7:]
'complex'
>>> d="codegnan it solutions"
>>> d[-21:-13]
'codegnan'
>>> d[-9:]
'solutions'
>>> #striding
>>> a="data science"
>>> a[::]
'data science'
>>> a[::1]
'data science'
>>> a[::2]
'dt cec'
