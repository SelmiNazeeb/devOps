def Sum_num(x):
    return sum(x)

def Higher_Order_Function(f,lst):
    var = f(lst)
    return var

result = Higher_Order_Function(Sum_num, [1,2,3,4]) 
print(result)
