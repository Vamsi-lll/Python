# biggest in the given list

#app-1 (using inbuilt functions)
""" def Max(lst):
    return max(lst) """

#app-2 (using sort function)
""" def Max(lst):
    if type(lst) != list:
        return 'pls enter valid formate'
    else:
        lst.sort()
        return lst[-1] """
        
#app-3 (with out using any predefine function)

def Max(lst):
    j=0
    if type(lst)!=list:
        return 'pls enter valid formate'
    else:
        for i in lst:
            if i>j:
                j=i
        return j
    
print(Max([3,5,6,2,1,8,4,9]))
