def line(length=10, symbol="*"):
    print(length*symbol)


def L_Triangle(length=10, symbol=" *"):
    for i in range(1, length+1):
        print(i*symbol)


def RL_Triangle(length=10, symbol=" *"):
    for i in range(length, 0, -1):
        print(i*symbol)


def R_Triangle(length=10, symbol=" *"):
    for i in range(1, length+1):
        print("  "*(length-i) + symbol*i)


def FillSquare(length=10, symbol=" *"):
    for i in range(length):
        print(length*symbol)


def Hol_Square(length=10, symbol=" *"):
    for i in range(length):
        if i == 0 or i == length-1:
            print(length*symbol)
        else:
            print(symbol + "  "*(length-2) + symbol)
            
            

def Floyd_Triangle(length=5):
    start = 1
    end = 2
    for i in range(length):
        for j in range(start, end):
            print(j, end=" ")
        start = end
        end = start + i + 2
        print()


