Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #indexing-postive and negitive
>>> #indexing
>>> a="vijaywada"
>>> a[0]
'v'
>>> a[2]
'j'
>>> a[6]
'a'
>>> a[8]
'a'
>>> a[0]+a[1]+a[2]+a[3]+a[4]
'vijay'
>>> b="I am in class"
>>> a[8]+a[9]+a[10]+a[11]+a[12]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a[8]+a[9]+a[10]+a[11]+a[12]
IndexError: string index out of range
>>> b="I am in class"
>>> b[8]+b[9]+b[10]+b[11]+b[12]
'class'
>>> a[5]+a[6]
'wa'
>>> b[5]+b[6]
'in'
>>> b[1]
' '
>>> b[1]+b[4]+b[7]
'   '
c="i am learning python"
c[5]+c[6]+c[7]+c[8]+c[9]+c[10]
'learni'
c[14]+c[15]+c[16]+c[17]+c[18]+c[19]
'python'
d="codegan it solutions"
d[0]+d[1]+d[2]+d[3]
'code'
d[11]+d[12]+d[13]+d[14]+d[15]+d[16]+d[17]+d[18]+d[19]
'solutions'
d[12]+d[13]+d[14]+d[15]+d[16]+d[17]+d[18]+d[19]
'olutions'
d[11]+d[12]+d[13]+d[14]+d[15]+d[16]+d[17]+d[18]
'solution'
a="time is very precious"
a[-1]+a[-2]+a[-3]+a[-4]+a[-5]+a[-6]+a[-7]+a[-8]
'suoicerp'
a[-8]+[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a[-8]+[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
TypeError: can only concatenate str (not "list") to str
a[-21]+a[-20]+a[-19]+a[-18]
'time'
a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'precious'
a[-13]+a[-12]+a[-11]+a[-10]
'very'
a="hello hi how are you"
#you,hello,how
a[-3]+a[-2]+a[-1]
'you'
a[-9]+a[-10]a[-11]
SyntaxError: invalid syntax
a[-9]+a[-10]+a[-11]
'woh'
a[-11]+a[-10]+a[-9]
'how'
a[-16]+a[-15]+a[-14]+a[-13]+a[-12]
'o hi '
a[-20]+a[-19]+a[-18]+a[-17]+a[-16]
'hello'
a="codegnan"
a[0]+a[1]+a[2]+a[3]
'code'
a[0:3]
'cod'
#we should give extra number for slicing if string ends with 7 we have to give 8
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a="work until you succeed"
a[0:4]
'work'
a[5:10]
'until'
a[7:10]
'til'
a[12:15]
'ou '
a[11:15]
'you '
a[11:14]
'you'
a[16:]
'ucceed'
a[15:]
'succeed'
b="simple is better than complex"
b[0:6]
'simple'
b[7:8]
'i'
b[7:9]
'is'
[10:16]
SyntaxError: invalid syntax
b[10:16]
'better'
b[17:21]
'than'
b[22:]
'complex'
b[22:29]
'complex'
a="vizag is city of destiny"
a[-7:]
'destiny'
a[-7:0]
''
a[-9:-11]
''
a[-10:-8]
'of'
a[-24:-19]
'vizag'
a[-18:-16]
'is'
a[-15:-11]
'city'
b="vijayawada is a royal city"
b[-5:]
' city'
b[-4:]
'city'
b[-10:-7]
'roy'
b[-10:-6]
'roya'
b[-10:-5]
'royal'
b[-15:-13]
'is'
b[-26:-15]
'vijayawada '
[-26:-14]
SyntaxError: invalid syntax
#striding
#[a:b:c]-start,and,increment
a="Data Science"
a[::]
'Data Science'
a[::1]
'Data Science'
a[::2]
'Dt cec'
a="machine learning"
a[::5]
'mnag'
a[::7]
'm n'
a[::2]
'mcielann'
a[::6]
'men'
a[7:]
' learning'
a[:9]
'machine l'
a[6:11]
'e lea'
a[2:8]
'chine '
a[5:12]
'ne lear'
a="cloud computing"
a[1:10:2] #first we have to do slicing and based on last num we increment it.and in postive string highest to lowest not possible and in negitive striding lowest to highest not possible
'lu op'
a[2:13:3]
'o mt'
a[5:14:4]
' pn'
a[3:12:6]
'up'
a[-1:-9:-2]
'gium'
a[-4:-13:-5]
'tc'
a[-2:-12:-3]
'nuod'
