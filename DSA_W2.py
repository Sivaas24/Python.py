'''
Smallest of 3 numbers
Check whether a number is Prime
Print all Prime numbers from 1 to N
Count the factors of a number
Find GCD / HCF of two numbers
Find LCM of two numbers
Print Fibonacci series
Check whether a number is Armstrong
Find the Largest digit in a number
Find the Smallest digit in a number
Count the frequency of a digit
Remove a specific digit from a number
Find the Second Largest number in a list
Find duplicate elements in a list
'''

# Find smallest of 3 numbers
'''
a=int(input())
b=int(input())
c=int(input())
smallest=a
if b < smallest :
    smallest = b
if c < smallest :
    smallest = c
print(smallest)
'''

# Check whether a number is Prime
'''
n = int(input("Enter: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")
'''

# Print all prime numbers from 1 to N
'''
n = int(input("Enter: "))
for num in range(2, n + 1):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        print(num)            
'''

# Count the Factors of a Number
'''
n= int(input("Enter :"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
print(count)'''

# Find GCD / HCF of Two Numbers
'''
a=int(input())
b=int(input())
gcd=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0 :
        gcd=i
print(gcd)        
'''

# Find LCM of two numbers
'''
a=int(input())
b=int(input())

if a>b:
    largest=a
else:
    largest=b
lcm=0
for i in range(largest,a*b+1):
    if i%a==0 and i%b==0:
        lcm=i
        break
print(lcm)

'''

# Print Fibonacci series
'''
num=int(input())
first=0
second=1
for i in range(0,num):
    print(first)
    next=first+second
    first=second
    second=next

'''
# Check whether a number is Armstrong
'''
n =int(input())
sum=0
origianl =n
while n>0:
    ams=n%10
    sum=ams*ams*ams+sum
    n=n//10
if origianl == sum:
    print("amstrong")
else:
    print("Not amstrong")'''
    
# Find the Largest digit in a number
'''
n=int(input())
largest=0
while n>0:
    last=n%10
    if last > largest:
        largest=last
    n=n//10
print(largest)'''


# Find the Smallest digit in a number
'''
n=int(input())
smallest=9
while n>0:
    last=n%10
    if last<smallest:
        smallest=last
    n=n//10
print(smallest)
        '''
# Count the frequency of a digit

'''n=int(input())
target=int(input())
count=0
while n>0:
    last=n%10
    if target==last:
        count=count+1
    n=n//10
print(count)'''
    
# Remove a specific digit from a number
'''
n = int(input())
target = int(input())
result = 0
while n > 0:
    last = n % 10
    if last != target:
        result = result * 10 + last
    n = n // 10
reverse = 0
while result > 0:
    last = result % 10
    reverse = reverse * 10 + last
    result = result // 10
print(reverse)
'''     

# Find the Second Largest number in a list

numbers = [10, 5, 8, 20, 15]
largest = 0
second = 0
for i in numbers:
    if i > largest :
        = largest







































