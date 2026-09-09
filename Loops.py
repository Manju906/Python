#loops
#for,while,range,break,continue,pass
#for loop()-sequence order
#list
'''a=[10,20,30,40,50]
for i in a:#i is temporary variable
    print(i)'''
'''a=[10,20,30,40,50,60]
for i in a:
    print(a)#if we keep print in place of i many times it will be printed'''
'''a=[10,20,30,40,50,60]
for i in a:
    print(i,end=" ")#by using end the output will print in one line
print(type(a))#this line should write outside for loop if not it will print type for every number
print(type(i))'''
'''a=[7,8,9,10,11]
for i in a:
    print(i)
print(type(a))
print(type(i))'''
#tuple
'''a=(7,8,9,10,11)
for i in a:
    print(i)
print(type(a))
print(type(i))'''
#set()
'''b={4,5,6,7,8}
for i in b:
    print(i)
    print(type(b))
    print(type(i))'''
#dictionary
'''a={"name":"manju","year":2026,"month":8}
for i in a:
    print(i)
print(type(a))
print(type(i))'''
#dict methods
'''a={"name":"manju","year":2026,"month":8}
for i in a:
    print(i)
for i in a.keys():
    print(type(a))
    print(type(i))'''
'''a={"name":"manju","year":2026,"month":8}
for i in a:
    print(i)
for i in a.values():
    print(type(a))
    print(type(i))'''
'''a={"name":"manju","year":2026,"month":8}
for i in a:
    print(i)
for i in a.items():
    print(type(a))
print(type(i))'''
'''a="codegnan"
for i in a:
    print(i)
print(type(a))
print(type(i))'''
'''a="codegnan"
for i in a:
    print(i,end="")
print(type(a))
print(type(i))'''
'''a=[4.5,6.7]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''
'''a=['apple','banana']
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''
'''a=[5+9j,6+2j]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''
'''a=[True,False]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''
'''a=[4,5.6,"python",3+2j,True,False]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''
#task
a=["codegnan","python","course"]
#o/p:CODEGNAN,PYTHON,COURSE
'''b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=" ,")'''

'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''

'''name=input("enter your name:")
mobile_no=int(input("enter your mobileno:"))
mailid=input("enter your mail:")
collegename=input("enter collegename:")
branch=input("enter your branch:")
print("....................Student Profile.................")
print("name is",name)
print("mobileno is",mobile_no)
print("mailid is",mailid)
print("collegename is",collegename)
print("branch is",branch)'''


#while()-continues iteration
'''a=10
while a>1:
    print(a)'''
'''a=10
while a<5:
    print(a)'''
'''a=10
while a>1:
    print(a)
    a=a-1'''#prints upto 2 to satisfy the condition given 
'''a=10
while a>1:
    a=a-1
    print(a)'''#o/p:prints upto 1 because we have used the condition before print statement

#decrement(assignment operator)
'''a=20
while a>2:
    print(a)#for decrement a value should be more
    a-=1'''

'''a=20
while a>2:
    print(a)#for increment a value should be low 
    a+=1'''
#runtime
'''while True:
    age=int(input("Enter age:"))
    if age>=18:
        print("Eligible to vote")
    else:
        print("Not Eligible to vote")'''
'''while True:
    n=int(input("Enter n value:"))
    if n%2==0:
        print("It is Even")
    else:
        print("Is is odd")'''

#range()
#start stop step
'''for i in range(5):
    print(i)'''

'''for i in range(5,50):
    print(i)'''

#tasks
'''for i in range(0,20,2):
    print(i)'''

'''for i in range(3,30,3):
    print(i)'''

'''for i in range(5,50,5):#when we use step we should use step number as difference not next number
    print(i)'''


#grade code'
'''while True:
    marks=int(input("Enter the marks:"))
    if marks in range(91,101):
        print("Grade A")
    elif marks in range(81,91):
        print("Grade B")
    elif marks in range(71,81):
        print("Grade C")
    elif marks in range(51-70):
        print("Grade D")
    else:
        print("Failed")'''

#break-used to terminate the code
'''a=30
while a>10:
    print(a)
    a=a-1
    if a==20:
        break'''
'''for i in range(35):

    if i==30:
        break
    print(i)'''
a="python"
'''for i in a:
    if i=="h":
        break
    print(i)'''

#continue
'''a=40
while a>20:
    a=a-1
    if a==25:
        continue
    print(a)'''

'''a="python"
for i in a:
    if i=="t":
        continue
    print(a)'''

#pass
'''a=10
while a>1:
    a=a-1
    if a==5:
        pass
    print(a)'''

'''for i in range(10):
    if i==4:
        pass
    print(i)'''

#patterns
'''for i in range(4):
    for j in range(3):
        print("*",end=" ")
    print()'''
'''for i in range(4):
    i=i-1
    for j in range(3):
        print("*",end=" ")
    print()'''

'''for i in range(4,0,-1):
    for j in range(3):
        print("*",end=" ")
    print()'''
'''for i in range(1,6,2):
    for j in range(3):
        print(i,end=" ")
    print()'''

'''for i in range(1,6,2):
    for j in range(3,0,-1):
        print(j,end=" ")
    print()'''



