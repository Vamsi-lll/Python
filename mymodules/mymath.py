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


""" ===========================================       Areas       ================================ """
# area of square
# Formula Side x Side
def AOSquare(side):
    side=int(side)
    return side*side

# area of rectangle
# Formula length x width
def AORectangle(length,width):
    return length*width

# area of circle
# Formula  pi(3.14159) x radius x radius
def AOCircle(radius):
    area= 3.14159*(radius**2)
    return area

# circumfrence of circle
# formula 2 x pi(3.14159) x radius
def COCircle(radius):
    circumfrence=2*3.14159*radius
    return circumfrence


# Area of traingle
# formula 1/2*base*height => 0.5 x base x height
def AOTraingle( *,base,height):
    area=0.5*base*height
    return area

""" ===========================================  perfect square or not ============================ """
def is_perfectSquare(num):
    for i in range(2,num+1):
        if int(num/i)==i:
            print(i)
            return True
    return False
