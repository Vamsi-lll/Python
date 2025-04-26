lst1=[1,2,3,4,5,6]
lst2=[6,7,8,9,10,11]
# aim is to extract the common elements from this two lists

#approch-1:

l1=set(lst1)
l2=set(lst2)
print(list(l1.intersection(l2)))

#approch-2:
lst3=[]
for i in lst1:
    if i in lst2:
        lst3.append(i)
print(lst3)
