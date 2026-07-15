Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dictionaries
>>> a={"name":"manju","year":2026,"month":7}
>>> print(a)
{'name': 'manju', 'year': 2026, 'month': 7}
>>> type(a)
<class 'dict'>
>>> #methods
>>> #keys
>>> a.keys()
dict_keys(['name', 'year', 'month'])
>>> a.values()
dict_values(['manju', 2026, 7])
>>> a.items()
dict_items([('name', 'manju'), ('year', 2026), ('month', 7)])
>>> b={"name","year"}
>>> type(b)
<class 'set'>
>>> #update
>>> a={"year":2026,"month":"july","date":14}
>>> a.update({"time":2})
>>> a
{'year': 2026, 'month': 'july', 'date': 14, 'time': 2}
>>> a.update({"time":2},{"day":"tue"})
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.update({"time":2},{"day":"tue"})
TypeError: update expected at most 1 argument, got 2
>>> a.update({"time":2,"day":"tue"})
>>> a
{'year': 2026, 'month': 'july', 'date': 14, 'time': 2, 'day': 'tue'}
#setdefault
a={"name":"manju","city":"vja"}
a.setdefault("mail","manjuharini@gmail.com")
'manjuharini@gmail.com'
a
{'name': 'manju', 'city': 'vja', 'mail': 'manjuharini@gmail.com'}
#pop
a={"state":"ap","country":"india"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("country")
'india'
a
{'state': 'ap'}
a.popitem()
('state', 'ap')
a
{}
#copy
a={"colour":"black","food":"biryani"}
a.copy()
{'colour': 'black', 'food': 'biryani'}
b=a.copy()
b
{'colour': 'black', 'food': 'biryani'}
len(a)
2
#dontallowduplicates#
a={"name":"manju","city":"vja","name":"manju"}
print(a)
{'name': 'manju', 'city': 'vja'}
a
{'name': 'manju', 'city': 'vja'}
a={"name1":"manju","city":"vja","name2":"manju"}
a
{'name1': 'manju', 'city': 'vja', 'name2': 'manju'}
a.count("name1")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.count("name1")
AttributeError: 'dict' object has no attribute 'count'
a.index("city")
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.index("city")
AttributeError: 'dict' object has no attribute 'index'
#clear
a.clear()
a
{}
b={}
b.update({"name:"manju"})
          
SyntaxError: unterminated string literal (detected at line 1)
b.update({"name:"manj"})
          
SyntaxError: unterminated string literal (detected at line 1)
#how to add more numbers of keys and values
          
