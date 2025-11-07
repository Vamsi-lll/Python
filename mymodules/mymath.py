""" =============================== mymath module for mathamatical operations ================= """

# for adding all numbers it accepts a seres of numbers which need to be unpacked while passing the numbers"
def Add_all(*num):
    init_num=0
    for i in num:
        init_num+=i
        
    return init_num


#  multiply all numbers it accepts a seres of numbers which need to be unpacked while passing the numbers
def mul_all(*num):
    init_num=1
    for i in num:
        init_num*=i
    return init_num


""" ========================================= Number Propertie ================================ """

# check wether the given number is even or not
def is_even(n):
    n=int(n)
    if n%2==0:
        return True
    else:
        return False

#check wether the given number is prime or not
def is_prime(n):
    n=int(n)
    if n<=2:
        return True
    elif n==3:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
            else:
                return True
            

""" =========================================== Number Range and List============================ """
# gives you the factroial of the given number 
def factroial_of(n):
    n=int(n)
    initial_num=1
    for i in range(1,n+1):
        initial_num*=i
    return initial_num



