# while syntax:

#initialization
# while condition:
#     #statement
#     #inc/dec

# i=1
# while i<=5:
#     print(i)
#     i+=1
# sum=0
# i=1
# while i<=10:
#     sum=sum+i
#     i+=1
# print(sum)

# even=0
# odd=0
# i=1
# while i<=10:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
#     i+=1
# print("Even = ",even)
# print("Odd = ",odd)

# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i," ",j)
 # Factorial 
# fact=1
# i=5
# while i>=1:
#     fact*=i
#     i-=1
# print(fact)

# username=""
# password=0
# while username!="admin" or password!= 12345:
#     username=input("Enter the username : ")
#     password=int(input("Enter the password : "))

# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1)+fib(n-2)
# n=int(input("Enter the number : "))
# print(fib(n))

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
# #     for j in range(1,1+n):
# #         print(chr(96+i),end=" ")
# #     print()

# list=[5,3,6,7,8,9]
# list.sort()
# print(list)
# print(list[-2])
# print(list[-3])

list=[5,0,5,3,0,1,2]
list.sort(reverse=True)
print(list)