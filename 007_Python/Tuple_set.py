#### TUPLE ####

# data_constant = ("monday","tuesday","wednesday")
# data_constant2 = ("thursday","friday","saturday")
# print(data_constant[1:3])
# print(data_constant + data_constant2)
# print(data_constant2[0])
# print(list(data_constant))  #convert to list
# data_constant3 = tuple("sunday")    #print string to each characters like each are elements in a tuple("s","u","n","d","a","y")
# print(data_constant3)
# print(data_constant2*2)


### SET #####

data_set = set()
print(type(data_set))

for i in range(1,8):
    data_set.add(i)

for i in data_set:
    print(i)

print(len(data_set))

data_set.pop()
print(len(data_set))


