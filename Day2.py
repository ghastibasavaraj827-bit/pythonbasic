# # Tuple - Immutable - stores orderwise data
# # mytuple=("Basu","Akash","Pramod",3.14,89,"Mahi")
# # print(mytuple)
# # print(type(mytuple))
# # print(mytuple[3])
# # mytuple[0]="Ghasti"

# # myset={"Basu","Akash","Pramod",3.14,89,"Mahi"}
# # print(myset)
# # print(type(myset))
# # myset.add(60)
# # print(myset)
# # myset.add(60)
# # print(myset)
# # myset.discard(49) # It don't affect original set and it don't raise error
# # myset.remove(49)
# # # print(myset)
# # set1={1,2,3,4,5,}
# # set2={6,5,1,9,10}
# # # newset=set1.union(set2) #It combines both the set
# # # print(newset)
# # # newset=set1.intersection(set2) #It returns the common element from both the set
# # # print(newset)
# # # newset=set1.difference(set2) #It returns the elements that present in first set and not in the second set
# # # print(newset)
# # set1.pop()
# # set1.pop()
# # set1.pop()
# # print(set1)
# # set2.clear()
# # print(set2)

# # Dictionary - mutable

# mydict={"name":"Basu","city":"Belagavi"}
# # # print(mydict)
# # # print(mydict["name"])
# # # mydict["name"]="Rahul"
# # # print(mydict)
# # # mydict["age"]=18
# # # print(mydict)
# # # mydict["age"]

# # # mydict={
# # #     101:"prashant",
# # #     102:"ashish",
# # #     "103":"mohini",
# # #     "104":"trivani",
# # #     101:"ashish",
# # #     104:"ashish"
# # # }
# # # print(mydict)
# # # a=mydict["104"]
# # # print(a)
# # # mydict[102]="Adam"
# # # print(mydict)
# # # for x in mydict:
# # #     print(x,mydict[x])
# # # for x in mydict.values():
# # #     print(x)
# # # for x,y in mydict.items():
# # #     print(x,y)
# # # mydict[108]="Pramod"
# # # print(mydict)
# # mydict.pop("name")
# # print(mydict)
# newdict=mydict.copy()
# print(newdict)