
    #if else
num=int(input("enter the number : "))
if num>10:
    print("number is greater than 10")
elif num<10 and num>1:
    print("less than 10")
else:
    print("out of range")



    # while loop
num = int(input("enter the number : "))
i=1
while i<=10:
    print(num*i)
    i=i+1
else:
    print("done")   #print at the end of while loop


for i in range (5):
    if i==3:
        pass  #similar to continue 
              #but pass can use in anything like loop or function it will execute a null value
              #continue is like skip a line,it can use in loop only
    else:
        print(i)  #output 0,1,2,4
        