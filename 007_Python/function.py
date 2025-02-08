def hello_world():
    print("hello world")
hello_world()       #output - hello world


def hello_world(message):
    print(message)
hello_world("here we go again")     #output - here we go again

    #sum
def hello_world(nums):
    sum = 0
    for i in nums:
        sum+=i
    print(sum)
hello_world([1,2,3,4]) 

    #prime number
def prime_num(num):
    for i in range(2,num//2):
        if num%i==0:
            print("not prime")
            return
    print("prime")
prime_num(23)

    #find first repeating element in list
def repeating(nums):
    store=list()        #instead of 'list()' we can use 'set()'
    for i in nums:
        if i in store:
            print(i)
            return
        store.append(i) # for set() 'append()' will replaced as 'add()'
repeating(["1","2","3","3","4","1"])


