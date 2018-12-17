#Allan Krasner

import re
print("EXERCISE 1\n")
print(5/3) #5 divided by 3
#This statement divided 5 by 3 and returns the exact value even as a decimal
print(5%3) #5 mod three returns the remainder
# This statement finds the reminder of 5 / 3
print(5.0/3) #5 divided by 3
# This statement works just like the first one. It returns the exact decimal value
print(5/3.0) #5 divided by 3
# This statement is just as valid as the one above. It returns an exact decimal value
print(5.2%3) #5.2 mod 3
# This statement returns the exact decimal remainder of 5.2 / 3

print("\nEXERCISE 2\n")
# print(2000.3**200)#2000.3 to the 200th power
#This statement returns 2000.3 to the 200th power but needed to be commented out because of its size
print(1.0+1.0-1.0)#1+1-1
#This statement adds and subtracts doubles to get a double
print(1.0 + 1.0e20 - 1.0e20)
#This statement adds a large number to 1 and it gets too big. Returns 0.

print("\nEXERCISE 3\n") 
x = float(123)
print(x)
x = float('123')
print(x)
x = float('123.23')
print(x)
x = int(123.23)
print(x)
#x = int('123.23') #returns an error
#print(x)
x = int(float('123.23')) #no error
print(x)
x = str(12)
print(x)
x = str(12.2)
print(x)
x = bool('a') #true
print(x)
x = bool(0) #false
print(x)
x = bool(0.1) #true
print(x)

print("\nEXERCISE 4\n")
print(range(5))#This statement returns the range from 0 to 5
print(type(range(5)))#The type returned it's own type of range

print("\nEXERCISE 5\n")
number = 0
x = 11
while number < 20:
    if x % 5 is 0 or x%7 is 0 or x%11 is 0:
        print(x)
        number+=1
    x+=1

print("\nEXERCISE 6\n")
def is_prime(n):
    for i in range(2, int(n/2)):
        if n % i == 0:
            return False
            break
    return True

print(is_prime(29))
print(is_prime(32))

def is_prime_improved(n):
    if n is 2 or n is 3:
        return True
    elif (n-1)%6 is 0 or (n+1)%6 is 0:
        if(is_prime(n)):
            return True
        else:
            return False
    else:
        return False

print(is_prime_improved(29))
print(is_prime_improved(32))
def get_primes(n):
    l=[]
    for x in range(n):
        if(is_prime_improved(x)):
            l.append(x)
    return l

print(get_primes(30))

def get_n_primes(n):

    if n <= 0:
        return []
    elif n is 1:
        return [2]
    elif n is 2:
        return [2,3]
    else:
        x=2
        l = [2,3]
        num = 5
        while x < n:
            if(is_prime_improved(num)):
                l.append(num)
                x+=1
            num += 2
    return l

print(get_n_primes(10))

print("\nEXERCISE 7\n")
def print_list(l):
    str = ""
    for each in l:
        str = str + "%d, " % each
    print(str)

print([2,7,5,4,2])

def print_reverse(l):
    str = ""
    for each in l[::-1]:
        str = str + "%d, " % each
    print(str)

print_reverse([2,7,5,4,2])

def len(l):
    count = 0;
    for each in l:
        count += 1;
    return count;

print(len([5,4,7,2]))

print("\nEXERCISE 8\n")
a = [4,5,9,3,1,6,8]
b=a

b[0] = 10
print(a[0])
#a[0] was updated when b[0] was updated

c = a[:]
c[2] = 10
print_list(a)
#a wasn't affected when c was updated

def set_first_elem_to_zero(l):
    l[0] = 0
    return l

set_first_elem_to_zero(a)
print(a)
#the first element becomes a zero

print("\nEXERCISE 9\n")
def concat(A):
    l = []
    for each in A:
        l += each
    return l
print(concat([[1,3],[3,6]]))
print(concat([[4,8,6,5],[4,21,5],[2,8]]))

print("\nEXERCIES 10\n")
import matplotlib.pyplot as plt
import numpy as np

y = (np.sin(x-2)*np.sin(x-2))*np.e*np.exp(-x*np.exp(2))
plt.plot(x, y)
plt.title('Function')
#plt.ylimit(0,2)
#plt.xlimit(0,2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

print("\nEXERCISE 11\n")
def iteration(l):
    p = 1
    for each in l:
        p *= each;
    return p

print(iteration([1,2,3,4]))

def recursion(l):
    if(len(l)==1):
        return l[0];
    else:
        return l[0]*recursion(l[1:])

print(recursion([1,2,3,4]))

print("\nEXERCISE 12\n")
def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(20))

print("\nEXERCISE 13\n")

file  = open("emails.txt", "r")

print(re.search('[a-zA-Z]*@[a-zA-Z]*\.[a-zA-Z]*', 'asdfd@asfsd.afs'))


for line in file:
    match = re.search('[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+', line)
    print(match)