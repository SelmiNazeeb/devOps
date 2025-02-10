def square(x):
    return x**2
def cube(x):
    return x**3
def absolute(x):
    if x>0:
        return x
    else:
        return -x

def Hof(type):
    if type=="square":
        return square
    if type=="cube":
        return cube
    else:
        return absolute

res = Hof('square')
res = Hof('cube')
res = Hof('absolute')
print(res(-5))
    