#global and local variables-A variable is inside and outside the function is called global and local variables.
#A variable is defined above the function and is accessible to the entire global space is called global variable.
#A variable is defined inside the function is called local variable.
#first case of global variable
'''a=5
def check():
    print("inside value is",a)
check()
print("outside value is",a)'''

#second case of global variable
'''a=2
def check1():
    a=5
    a=a**2
    print("inside value is",a)
check1()
print("outside value is",a)'''

#third case of both global and local variables
'''a=4
b=9
def check2():
    a=7
    print("inside value is",a)
    a=10
    print("update value is",a+5)
    b=12 #local variable because it is not defined outside the function
    b=b+a
    print("value of b is",b)
check2()
print("a value is",a)
print("b value is",b)'''

#usage of global keyword
'''when user wants to create a variable inside the function directly and carry forward the updated value outside
fun then global keyword is used.'''
'''a=3
def final():
    global a,b
    print("inside the value is",a)
    a=6
    print("updated value is",a)
    #global b 
    b=13
    b=b+a
    print("b value is ",b)
final()
print("value of a is",a)
print("value of b is",b)#if we dont give global for b it will print as error because b is declared inside the function'''


#diff btwn list c and tuple c
'''no tuple comprehension in above cases if we remove those braces and keep paranthesis then outcome is generator.
syntax:a=[exp for var in collection/range]
diff btwn list c and tuple c-we should use *var in print or datatype in print'''
'''a=[i for i in range(16)]
print(a)
print(type(a))'''

'''a=(i for i in range(16))
print(*a)
print(type(a))'''
#print(list(b))
#print(tuple(b))
#print(set(b))


#Generators
'''A generator is also a function which can be used as an iterator(loop) by producing grp of values and we can use
yield keyword'''

#yield v/s return
#return will terminate the function where as yield can pass the function and go on with every succesive iteration.
'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))''' #for yield in print we should use * before function

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        return a
        a=a+1
print(check(a,b))'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        #return a
    return a  
print(check(a,b))'''


#ex:yield v/s return
'''def mygen():
    return "python"
    return "java"
    return "dsa"
    return "python","java","dsa"
print(*mygen())'''


'''def mygen():
    yield "python"
    yield "java"
    yield "dsa"
#print(*mygen())
    

#next() is used to print values in new line only used in yield
d=mygen()
print(next(d))
print(next(d))
print(next(d))'''


#BMI
a=float(input("enter your weight:"))
b=float(input("enter your height:"))
n=a/(b)**2
print("Your bmi is",n)
if n<18.5:
    print("Underweight")
elif n>18.5 and n<=24.5:
    print("Normal Weight")
elif n>24.5 and n<=29.5:
    print("Over Weight")
elif n>30:
    print("Obesity")

