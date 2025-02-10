def missing_num(nums,n):
    total_sum=0
    for i in range(n):
        total_sum+=i
        return
    l=len(nums)
    list_sum=0
    for i in range(l):
        list_sum+=i
        return
    missing_num=total_sum-list_sum
    return missing_num
n=int(input("enter range"))
nums=list(map(int,input("enter input").split()))
missing_num(nums,n)
print(missing_num)