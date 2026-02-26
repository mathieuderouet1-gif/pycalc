import sys

op1 = float(sys.argv[1])
op = sys.argv[2]
op2 = float(sys.argv[3])

def addition(x : float,y : float)->float:
    a = x + y
    return a

if op == "+":
    addition(op1,op2)

def soustraction(x : float,y : float)->float:
    s = x - y
    return s

if op == "-":
    soustraction(op1,op2)

def multiplication(x : float, y : float)->float:
    m = x * y
    return m

if op == "*":
    multiplication(op1,op2)    

