'''a=10
b=20
print("the sum is",a+b)
print("the difference is",a-b)
print("the product is",a*b)
a=100
b=200
print("the sum is",a+b)
print("the difference is",a-b)
print("the product is",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the difference is",a-b)
print("the product is",a*b)'''


#functions
'''def calculate(a,b):
    print("the sum is",a+b)
    print("the difference is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

'''def cal(c,d):
    print("the division is",c//d)
    print("the mod is",c%d)
    print("the power is",c**d)
cal(2,3)
cal(5,9)
cal(7,11)'''

'''def cal(a,b): #simple version of using functions without using formatting
    print(a+b)
cal(2,8)'''

#while loop
'''while True:
    def add():
        a=int(input())
        b=int(input())
        print(a+b)
    add()'''

#runtime
'''def add():
    a=int(input("a val")) #recursive function will be used without using while loop
    b=int(input("b val"))
    print(a+b)
    add()
add()'''

'''def fullname():
    fname=input("fname")
    lname=input("lname")
    print((fname+" "+lname).title())
fullname()'''

#print v/s return
#return will terminate the function and gives back a value from the function can only be used one time only 
#print just shows the human user output in a console 
'''def mul(a,b):
    print(a*b)
mul(5,3)'''

'''def mul(a,b):
    return a*b #we can give values without brackets
print(mul(6,3))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    return d #gives only one value in output because it terminates after printing one value or to avoid that we can write all values in one return
    return e
print(cal(2,3))'''

'''def split(a,b):
    c=a//b
    return c
print(split(20000,10))'''

'''def split():
    a=int(input("a val"))
    b=int(input("b val"))
    c=a//b
    return c
print(split())'''

'''def split():
    a=int(input("a val"))
    b=int(input("b val"))
    c=b//a
    #print("the splitting of bill is",c)
    #print("the splitting of bill is {}".format(c))
    print(f"the splitting of bill is {c}")
split()'''


'''def split():
    a=int(input("a val"))
    b=int(input("b val"))
    print("the splitting of bill is {}".format(b//a))
    print(f"the splitting of bill is {b//a}")
split()'''

#patterns
'''right angle
*
* *
* * *
* * * *
* * * * *

reverse right angle
* * * * *
* * * *
* * *
* *
*

square
* * * *
* * * *
* * * *
* * * *

pyramid
   *
  *  *
 *  *  *

#right angle
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()'''

'''n=int(input())
for i in range(n+1):
    for j in range(i):
        print("*",end="")
    print()'''

#reverse right angle
'''for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()'''
'''n=int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()'''

#square
'''for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()'''
'''n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()'''
#pyramid
'''n=int(input())
for i in range(1,n+1):
        print(" "*(n-i)+"* "*i)'''

#keywords and positional arguments -realtime->google forms
#student details
#step1
#we can give values in code itself 
'''def details(id,name,mailid):
    id=10
    name="manju"
    mailid="manju@gmail.com"
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")'''

#step2
#we can give values at last also it will minimize the number of lines of code
'''def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
details(id="10",name="rupa",mailid="r@gmail.com")
details(id="11",name="vamsi",mailid="v@gmail.com")
details(id="12",name="jessi",mailid="j@gmail.com")'''

#step3
#we can give values without mentioning their vars in positional arguments
'''def details(id,name,mailid):
    print(id,name,mailid)
details(10,"manju","m@gmail.com")'''

#step4
#we can give in jumble order but it will print in jumble order only
'''def details(id,name,mailid):
    print(id,name,mailid)
details("manju","m@gmail.com",10)'''

#step5
#even after we give in jumble order if we give positional arguments it will print in order accordingly
'''def details(id,name,mailid):
    print(id,name,mailid)
details(name="manju",mailid="m@gmail.com",id=10)'''


#employee details
'''def emp_details(name,salary,dept):
    name="manju"
    salary=20000
    dept="a"
    print(name,salary,dept)
emp_details(name="name",salary="salary",dept="a")'''


'''def emp_details(name,salary,dept):
    print(name,salary,dept)
emp_details(name="manju",salary=20000,dept="a")'''


'''def emp_details(name,salary,dept):
    print(name,salary,dept)
emp_details("manju",20000,"a")'''


'''def emp_details(name,salary,dept):
    print(name,salary,dept)
emp_details("manju","a",20000)'''

'''def emp_details(name,salary,dept):
    print(name,salary,dept)
emp_details(name="manju",dept="a",salary=20000)'''


#default arguments
#we can pass aruguments without giving values
'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %d" %price)
Grocery("sugar",100)'''

#we can pass arguments without giving first value
'''def Grocery(item,price=600):
    print("item is %s" %item)
    print("price is %d" %price)
Grocery("sugar")'''

#we can pass both values in arguments itself
'''def Grocery(item="rice",price=2000):
    print("item is %s" %item)
    print("price is %d" %price)
Grocery()'''

#we cannot give second value as an empty it will raise error as non-def arg pass def arg
'''def Grocery(item="ghee",price):
    print("item is %s" %item)
    print("price is %d" %price)
Grocery(500)
Grocery("sugar",100)'''

#Task
#cake,price,qty-in default arguments
'''def Bakery(cake,price,quantity):
    print("cake is %s" %cake)
    print("price is %d" %price)
    print("quantity is %d" %quantity)
Bakery("red velvet",1200,2)'''

'''def Bakery(cake,price,quantity=2):
    print("cake is %s" %cake)
    print("price is %d" %price)
    print("quantity is %d" %quantity)
Bakery("red velvet",1200)'''

'''def Bakery(cake="red velvet",price=1200,quantity=2):
    print("cake is %s" %cake)
    print("price is %d" %price)
    print("quantity is %d" %quantity)
Bakery()'''




#*argument-used for unpack the elements and store the multiple values in one variable
'''a=[1,2,3,4,5,6,7]
print(a)
print(*a)'''

'''b=(1,2,3,4,5)
print(b)
print(*b)'''

'''c=[1,2,3,4,5,6]
print(c)
print(*c)'''

'''d={'name':'manju','id':2}
print(d)
print(*d)'''

'''a,b,c=1,2,3,4,5,6,7
print(a)
print(b)
print(c)''' #error

'''a,b,*c='codegnan'
print(a)
print(b)
print(*c)'''


#variable length arguments
#variable length arg are automatically stored in tuple and we use *arguments

'''def check(*a):
    print(a)
    print(type(a))
check()
b=[4,5,6,7,8]
check(*b)
c=(3,4,5,6)
check(*c)
d={5,6,7,8}
check(*d)
e={"year":2026,"month":9}
check(*e)'''

'''def check(*a):
    d=2
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check()
check(2,3,4,5,6,7,8)
check(2,3.4,5.3,6,2.2)
check(3,4,5,6,7,8,4.2,'pooja')'''

'''def check():
    a=int(input("a value"))
    b=int(input("b value"))
    option=int(input("choose the option 1.add 2.sub 3.mul"))
    if option==1:
        print(a+b)
    elif option==2:
        print(a-b)
    elif option==3:
        print(a*b)
check()'''

'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
option = int(input("choose the option 1.add 2.sub 3.mul"))
if option==1:
        print(a+b)
    elif option==2:
        print(a-b)
    elif option==3:
        print(a*b)
check()'''
'''n=int(input("give count:"))
present=0
absent=0
for i in range(1,n+1):
    i=input(f"student{i}: (present/absent) ")
    if i=='present':
        present+=1
    else:
        absent+=1
print("Total Students",n)
print("Presenties ", present)
print("absenties ", absent)'''



#* will automatically stores in tuple

#kwargs-key word variable len arguments
#** will automatically stores in dictionary
'''def Details(**a):
    print(a)
    print(type(a))
Details()'''

'''def Details(**a):
    print(a)
    print(type(a))
Details()
d={'idnos':[10,20,30,40],
   'names':['dinesh','suresh','naresh'],
   'status':['p','a','a']}
Details(**d)''' #prints whole dictionary


#to print particular values using for loop and dict methods
'''def Details(**a):
    print(a)
    print(type(a))
    for i in a:#keys using for loop
        print(i)
    for i in a.keys():#keys using dict method
        print(i)
    for i in a:
        print(a[i])#values using for loop
    for i in a:
        print(i,a[i])#keys and values using for loop
    for i in a.items():#keys and values using dict method
        print(i)
Details()
d={'idnos':[10,20,30,40],
   'names':['dinesh','suresh','naresh'],
   'status':['p','a','a']}
Details(**d)'''

'''def check(*a):
    d=2
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check()
check(2,3,4,5,6,7,8)
check(2,3.4,5.3,6,2.2)
check(3,4,5,6,7,8,4.2,'pooja')'''

#using * and ** in a single code
'''def Details(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
    for i,j in b.items():
        print("keys is",i)
        print("values is",j)
Details()
data=(2,3,4,5,6.2,"python",6+9j,True,False)
Details(*data)
c={'idnos':[10,20,30,40],
   'names':['dinesh','suresh','naresh'],
   'status':['p','a','a']}
Details(*c)
Details(*data,**c)'''

#max,min,sum
#print(max(3,4,5,6,7,9,20))
#print(min(2,3,6,7,9))
#print(sum(2+3+4+7+9)) #error
#we have to store values in var to perform sum
'''a=4,5,6,7,8,9
print(sum(a))'''
'''print(sum([4,5,6,7,8,9)])'''

#task
#marks analysis report
'''n=int(input("Enter the number of students:"))
mark=[]
for i in range(1,n+1):
    marks=int(input(f"Enter the student{i} marks"))
    mark.append(marks)
print("Marks Analysis Report",n)
print("Total number of students are",n)
print("Heighest Marks",max(mark))
print("Lowest Marks",min(mark))
print("Total Marks",sum(mark))
print("Average Marks",sum(mark)/n)'''







