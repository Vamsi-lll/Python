# approch-1
# using predefined modules

lst=[2,4,5,7,1,6,8,333,23]
print(f"biggest num  in the given list list {max(lst)}")


# approch-2
#uing own sorting and finding the biggest

big=0
new_list=[]
for i in lst:
    if i>big:
        big=i
        new_list.append(big)
print(f"biggest in the given list is {new_list[-1]}")
