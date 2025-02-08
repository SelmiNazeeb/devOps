##Find out the character whuch is most repeating in an array

def most_repeat(arr):
    char_count = {}         #method 1

    for char in arr:
        if char in char_count:
            char_count+=1
        else:
            char_count=1
    
    most_char = max(char_count,key=char_count.get)
    return most_char
   
    most_char = max(arr,key=arr.count)      #method 2
    return most_char


arr =['a','5','r','5','w','r','o','5']
result = most_repeat(arr)
print(result)


##########################################################

list = ['selmi','khaleeda','asna','abhirami']
s = list[1:]            #print from 2nd to last
print(s)
print(list[1:-1])      #skip first and last
print(list[::])         #print all


###### some differences ######

# remove (3)-> remove from end of list
# pop(),pop(4)-> remove from last and can give index to remove from particular Index
# insert(4,"goa") -> insert at particular index given
# append("goa") -> insert to last
# del arr[3]  -> delete from index 3
# list.clear()  -> clear all elements 
# list.copy()   -> copy the list
# list.extend(list2) -> {for list}
# concat -> list1 + list2   {for string}
# count()     -> occurence of element
# len()        -> ttal no of elements


### create a list of companies and print first,last and middle one

company = ['abc','xyz','ust','hij','qwe','opi']
length = len(company)
mid = length/2
print("first : " + company[0])
print("last : " + company[length-1])
print("middle : " + company[mid-1])


