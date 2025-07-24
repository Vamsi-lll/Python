#-------------------------------------------------------------- Line function --------------------------------------------------------

def Line(width=30,symbol=" * "):
    print(symbol*width)

""" ------------------------------------------------------------SQUARES--------------------------------------------------------------- """
#-------------------------------------------------------------- Square function ------------------------------------------------------

def Square(width=5,symbol=" * "):
    for i in range(width):
        print((" "+symbol+" ")*width)
        
#-------------------------------------------------------------- Border Square function -----------------------------------------------
def Border_square(width=5,symbol=" *"):
    for i in range(width):
        if i== 0 or i== width-1:
            print(symbol*width)
        else:
            print(symbol+("  "*(width-2))+symbol)

""" ----------------------------------------------------------------Rectangle----------------------------------------------------------- """     
#-------------------------------------------------------------- Rectangle function ---------------------------------------------------

def Rectangle(width=5,symbol="*"):
    for i in range(width):
        print((" "+symbol+" ")*(width-1))

#-------------------------------------------------------------- Left_traingle function -----------------------------------------------

def Left_traingle(width=5,symbol="*"):
    for i in range(width):
        print((" "+symbol+" ")*i)


#-------------------------------------------------------------- Left_Reverse_traingle function ---------------------------------------

def Left_Reverse_traingle(width=5,symbol="*"):
    for i in range(width):
        print((" "+symbol+" ")*width)
        width-=1
    
#-------------------------------------------------------------- Right_traingle function ----------------------------------------------

def Right_traingle(width=5,symbol="*"):
    for i in range(width):
        print(" "*(width-i)+symbol*i)

#-------------------------------------------------------------- Right_Reverse_traingle function --------------------------------------

def Right_Reverse_traingle(width=5,symbol="*"):
    for i in range(width):
        print(" "*i+symbol*(width-i))

        
#-------------------------------------------------------------- Pyramid function -----------------------------------------------     
def Pyramid(width=5,symbol=" *"):
    for i in range(width):
        print(" "*(width-i)+symbol*i)
        
#-------------------------------------------------------------- Pyramid_Reverse function --------------------------------------
def Pyramid_Reverse(width=5,symbol="*"):
    for i in range(width):
        print(" "*i+symbol*(width-i))



