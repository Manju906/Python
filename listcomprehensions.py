#list comprehension
a=["vja","hyd","vzg"]
#["VJA","HYD","VZG"]
'''print(a.upper())'''


'''b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=" ")'''

#syntax
#a=[expr for var in collection/range]
'''b=[i.upper() for i in a]
print(b)'''

#tasks
'''a=["python","java","ml"]
#["Python","Java","Ml"]
b=[i.title() for i in a]
print(b)'''

'''a=[1,2,3,5,6,8,12,13]
#[1,2,9,25,36,64,144,169]
b=[i*i for i in a] #i**2/pow(i,2)
print(b)'''


#if usage in list comprehension
'''b=[i for i in range(16) if i%2==0]
print(b)'''

'''fruits=["apple","grapes","kiwi","mango","banana","berry"]
#b=[i for i in fruits if "a" in i]
b=[i for i in fruits if "a" not in i]
print(b)'''


#no elif usage in list comprehension

#if-else usage in list comprehension
'''b=[i*i if i%2==0 else i*5 for i in range(21)] 
print(b)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
#6,6,6,6,6
#c=[a[i]+b[i] for i in range(len(a))]
'''c=[a[i]+b[i] for i in range(5)]
print(c)'''


#ATM APPLICATION
'''account=100000
card=input("Insert the card:")
password=int(input("Enter the password:"))
options=int(input("Enter the options:"))
print("Insert the card")
if card=="c":
        print("Welcome Manju")
else:
    print("Incorrect card")
if password=="1234":
        print(''Options:1.Balance Enquiry
                             2.Withdraw'')
if options==1:
    print(f"Your Account Balance is:{account}")
elif options==2:
    withdraw=input("Enter the withdraw amount:")
    rem=account-withdraw
    print(rem)'''


'''while True:
    account=100000
    card=input("Insert the card:")
    if card=="c":
        print("Welcome Manju")
        password=int(input("Enter the password: "))
        if password==1234:
            print(''Option 1.Balance Enquiry
                      2.Withdraw'')
            options=int(input("Enter the option: "))
            if options==1:
                print(f"Your Account Balance is: {account}")
            elif options==2:
                withdraw=int(input("Enter the withdrawal amount: "))
                rem=account-withdraw
                print(f"Remaining balance: {rem}")
            else:
                print("Invalid option")
                break
        else:
            print("Incorrect password")
    else:
        print("Incorrect card")'''
