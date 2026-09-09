#built-in functions
#sum(),max(),min(),print(),len(),next(),input(),help(),range(),type()
#directory is collection of files
#print(dir())

#print(dir("__builtins__"))

#fromkeys-dict method
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a)) #dict cant be possible bcz its always keys and values

b=dict.fromkeys(a)
print(b)

b=dict.fromkeys(a,"python")
print(b)

b["t"]="manju"
print(b)'''

#zip()-we can combine multiple collections into one collection
'''a=[10,20,30,40,50]
names=["manju","roopa","eva","jessi","elsie"]
print(a+names)

b=zip(a,names)
#print(b)
print(*b)

c=list(zip(a,names))
print(c)

c=tuple(zip(a,names))
print(c)'''

#enumerate()-we can add counter to the collection
names=["harish","manish","sathish","ritesh","mukesh"]
'''for i in range(len(names)):
    print(i)'''#o/p:0,1,2,3,4

'''names=["harish","manish","sathish","ritesh","mukesh"]
for i in range(len(names)):
    print(i,names[i])'''

'''b=dict(enumerate(names))
print(b)

b=dict(enumerate(names,10))
print(b)'''

'''b=list(enumerate(names))
print(b)

b=tuple(enumerate(names))
print(b)

b=set(enumerate(names))
print(b)'''


#ascii-american standard code for information interchange
#ASCII
#chr-in brackets number should be given.
#ord-in brackets letter should be given.

#task
'''print(chr(97))
print(chr(122))

print(ord("A"))
print(ord("Z"))

print(ord(56))#error
print(char("a"))#error '''

'''for i in range(65,125):
    print(chr(i),end=" ")'''

'''for i in range(65,91):
    print(chr(i),end=" ")'''

'''for i in range(97,123):
    print(chr(i),end=",")'''

'''name=input()
for i in (name):
    print(i,ord(i))'''





