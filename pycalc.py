import sys

op1 = float(sys.argv[1])
op = sys.argv[2]
op2 = float(sys.argv[3])

def addition(x : int,y : int)->int:
    a = x + y
    return a

if op == "+":
    addition(op1,op2)



