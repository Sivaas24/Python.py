'''
Print numbers from 1 to N
Print numbers from N to 1
Print even numbers from 1 to N
Print odd numbers from 1 to N
Find sum of 1 to N
Find sum of even numbers
Find sum of odd numbers
Find factorial of a number
Count digits in a number
Find sum of digits
Reverse a number
Check palindrome number
Check even/odd
Check positive/negative/zero
Find largest of 3 numbers
'''



# Print numbers from 1 to N
''''
n=int(input(""))

for i in range(1,n+1):
    print(i,end=" ")
'''
# Print numbers from N to 1
'''
n=int(input(""))

for i in range(n,0,-1):
    print(i,end=" ")
'''
# Print even numbers from 1 to N
'''
n=int(input(""))

for i in range(1,n+1):
    if i%2==0:
        print(i,end=" ")
'''

# Print odd numbers from 1 to N
'''
n=int(input(""))

for i in range(1,n+1):
    if i%2!=0:
        print(i,end=" ")
'''

# Find sum of 1 to N
'''
n = int(input("Enter :"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
'''

# Find sum of even numbers
'''
n = int(input(""))
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum=sum+i
print(sum)
'''

# Find factorial of a number
'''
n = int(input("Enter :"))
sum=1
for i in range(1,n+1):
    sum=sum*i
print(sum)
'''

# Count digits in a number
'''
num = int(input("Enter :"))
count=0
while num>0:
    num=num//10
    count=count+1
print(count)
'''

# Find sum of digits
'''
n=int(input(''))
sum=0
while n>0:
    last=n%10
    sum=sum+last
    n=n//10
print(sum)
'''

# Reverse a number

'''n=int(input(''))
reverse=0
while n>0:
    last=n%10
    reverse=reverse*10+last
    n=n//10
print(reverse)'''


# Check Palindrome Number
'''
n=int(input(''))
Original=n
reverse=0
while n>0:
    last=n%10
    reverse=reverse*10+last
    n=n//10
if reverse == Original :
    print("Palindrome")
else:
    print("Not palindrome")

'''
#  Find the Largest Digit

'''
n = int(input("Enter number: "))
largest = 0
while n > 0:
    last = n % 10
    if last > largest:
        largest = last
    n = n // 10
print(largest)
'''



    

















