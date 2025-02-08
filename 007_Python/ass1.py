#create a list of furits and sort it

fruits = ["Apple","orange","kiwi","mango","banana"]
fruits.sort()     #doesnot return new list,it sorted in orginal itself.  
print(fruits)
l = sorted(fruits)    #sorted can't directly given to print.assign a variable and print.orginal list remains same
print(l)
fruits.sort(reverse=True)    #reverse the list
print(fruits)

#You have a list of numbers and find the largest and smallest among the list

num = ['2','7','4','5','1']
num.sort()          #method 1
length=len(num)
print("min : " + num[0] )
print("max : " + num[length-1] )
print(max(num))       #method 2
print(min(num))


## find nth largest and nth smallest among list without using sort###
def nsmall(arr,n):
    for _ in range(n):
        small = None
        for i in arr:
            if small == None or i<small:
                small = i
        new_arr=[]
        for x in arr:
            if x!=small:
                new_arr.append(x)
        arr = new_arr
    return small 

def nlarge(arr,n):
    for _ in range(n):
        large = None
        for i in arr:
            if large == None or i>large:
                large = i
        new_arr=[]
        for x in arr:
            if x!=large:
                new_arr.append(x)
        arr = new_arr
    return large

arr = ['3','5','7','2','1']
print(nlarge(arr,2))
print(nsmall(arr,3)) 


    





