Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary{}
a={"name":"manju","year":2026,"month":8}
print(a)
{'name': 'manju', 'year': 2026, 'month': 8}
type(a)
<class 'dict'>
b={"name","year","month"}
type(b)
<class 'set'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['manju', 2026, 8])
a.items()
dict_items([('name', 'manju'), ('year', 2026), ('month', 8)])
a={"year":2026,"month":8}
a.update({"date":20})
a
{'year': 2026, 'month': 8, 'date': 20}
a.update({"time":10}{"hour":1})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a.update({"time":10,"hour":1})
a
{'year': 2026, 'month': 8, 'date': 20, 'time': 10, 'hour': 1}
#in update we give in flower brackets but in set default we will give in round brackets
#setdefault
a={"name":"manju"}
a.setdefault("city","vja")
'vja'
a
{'name': 'manju', 'city': 'vja'}
#in dictionary already value unte update avvadhu if no update avthundhi
a={"name":"manju","age":23,"marks":80}
a
{'name': 'manju', 'age': 23, 'marks': 80}
a.pop(1)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.pop(1)
KeyError: 1
a.pop("age")
23
a
{'name': 'manju', 'marks': 80}
a.popitem()
('marks', 80)
a
{'name': 'manju'}
a.clear()
a
{}
del a
a
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a
NameError: name 'a' is not defined
#because it is already deleted.
#multiple values
a={"idnos":[10,20,30],"names":["sneha","priya","pooja"]}
type(a)
<class 'dict'>
a.keys()
dict_keys(['idnos', 'names'])
a.values()
dict_values([[10, 20, 30], ['sneha', 'priya', 'pooja']])
a.iems()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.iems()
AttributeError: 'dict' object has no attribute 'iems'. Did you mean: 'items'?
a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['sneha', 'priya', 'pooja'])])
>>> a
{'idnos': [10, 20, 30], 'names': ['sneha', 'priya', 'pooja']}
>>> a.pop("priya")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.pop("priya")
KeyError: 'priya'
>>> a.popitem()
('names', ['sneha', 'priya', 'pooja'])
>>> a
{'idnos': [10, 20, 30]}
>>> a.pop("ids")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a.pop("ids")
KeyError: 'ids'
>>> a.pop("idnos")
[10, 20, 30]
>>> a
{}
>>> a={"name":"manju","year":2026,"name":"harini"}
>>> a
{'name': 'harini', 'year': 2026}
>>> a={"name":"manju","year":2026,"name":"pooja"}
>>> a
{'name': 'pooja', 'year': 2026}
>>> a={"name1":"manju","year":2026,"name2":"pooja"}
>>> a
{'name1': 'manju', 'year': 2026, 'name2': 'pooja'}
>>> a.count("manju")
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.count("manju")
AttributeError: 'dict' object has no attribute 'count'
#dictionary does not allow duplicates so there is no count
len(a)
3
a
{'name1': 'manju', 'year': 2026, 'name2': 'pooja'}
a.copy()
{'name1': 'manju', 'year': 2026, 'name2': 'pooja'}
b=a.copy()
a
{'name1': 'manju', 'year': 2026, 'name2': 'pooja'}
b
{'name1': 'manju', 'year': 2026, 'name2': 'pooja'}
