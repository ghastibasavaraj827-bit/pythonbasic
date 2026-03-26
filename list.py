mylist=["Basu","Ajit","Karthik","Akash", "Sachin",30,30.9]
# print(mylist)
# print(mylist[0])
# print(mylist[-1])
# print(mylist[0:3])
# print(mylist[0:6:2])
# print(mylist[::-1])
# print(mylist[:5])
# mylist[2]="Rohit"
# print(mylist)
# if "Basu" in mylist:
#     print("Yes available")
# else:
#     print("Not available")
# mylist.append("Rohit")
#mylist.insert(1,"Sanket")
# mylist.remove("Akash")
# newlist=mylist.copy()
# # print(newlist)
# print(mylist)
#mylist=[["Basu","Ghasti"],[98.4],["November",18]]
# print(mylist)
# print(mylist[0][0])
# print(mylist[1][0])
mylist1=[20,23,32]
# # print(mylist+mylist1)
# # del mylist1[2]
# # print(mylist1)
# del mylist1
# print(mylist1)
# mylist1.clear()
# print(mylist1)
# name="Basavaraj"
# print(name)
# myname=list(name)
# print(myname)
# mylist1.reverse()
# print(mylist1)
# list=[23,2,45,23,98]
# list.sort()
# print(list)

# list.sort(reverse=True)
# print(list)
# #default it set to ascending
# #List should be homegeneous
# mylist=[2,3,4,5,6,]
# newlist=mylist
# print(newlist)
# print(id(mylist))
# print(id(newlist))
# newlist.append(8)
# print(mylist)
# for i in range(8):
#     print(i)
# for i in range(1,8):
#     print(i)
# for i in range(1,11,2):
# print(i)
# for i in range(1,11):
#     print(2*i,"",3*i,"","4*i","","5*i","","6*i","","7*i","","8*i","","9*i","","10*i")

#     print("11*i","","12*i","","13*i","","14*i","","15*i","","16*i","","17*i","","18*i","","19*i","","20*i")
# even=0
# odd=0
# for i in range(1,11):
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print("Even =", even)
# print("Odd = ",odd)
# username=input("Enter username: ")
# password=input("Enter password:")
# if username==password:
#     print("login successful")
# else:
#     print("login unsuccessful")

# brand=input("Enter brand name")
# if brand=="royal" or brand=="ROYAL":
#     print("RCB")
# elif brand=="birla" or brand=="BIRLA":
#     print("RR")
# else:
#     print("No Brand")
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))
if n1<n2 and n1<n3:
    print("n1 is smallestt number")
elif n2<n1 and n2<n3:
    print("n2 is smallest number")
else:
    print("n3 is smallest number")