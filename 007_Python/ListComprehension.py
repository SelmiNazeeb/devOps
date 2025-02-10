# lang = "Python"
# lst = list(lang)
# print(type(lst))
# print(lst)

# #list interpolation

# lst1 = [i for i in lang]
# print(lst1)
# print(type(lst1))

# lst2 = [i for i in range(20)]
# print(lst2)

# lst3 = [i*i for i in range(20)]
# print(lst3)

# lst4 = [(i,i*i) for i in range(10)]
# print(lst4)
# print(lst4[3][0])  #output - 3
# print(lst4[3][1])  #output - 9

# lst5 = [(i+2) for i in range (10)]
# print(lst5)

# lst6 = [i for i in range(20) if i%2!=0]  #odd
# print(lst6)

# lst7 = [i for i in range(20) if i%2==0]  #even
# print(lst7)

# lst8 = [i for i in range(30) if i%5==0 if i%2==0]  #even
# print(lst8)

# lst9 = [i for i in range(5,20) if i%2==0]  #even greater than 5 
# print(lst9)

# lst10 = [[1,2,3],[4,5,6],[23,24,56]]
# flat_list = [number for row in lst10 for number in row]
# print(flat_list)


    #lambda function

def sum(a,b):       #normal function
    return a+b
print(sum(2,7))

mySum = lambda a,b: a+b       #lambda function
print(mySum(2,6))

print((lambda a,b: a+b) (2,3))  #self invoking lambda
print((lambda a: a*a) (2))      #self invoking lambda function for find square


#example of lambda function in another function

def power(x):       #'x' in parameter taken by power function and 'n' is taken by lambda function. so when function is called,value is given in 2 bracket 
    return lambda n:x**n    
print(power(5)(3))






