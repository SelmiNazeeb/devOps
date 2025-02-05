# MultilineString = '''I am a intern in UST.
# type: ignore # I want to become the CEO of UST,
# That is why I am studying so hard.
# '''
# print(MultilineString)

###############################################################

# FName = 'Selmi'
# LName = 'Nazeeb'
# print(FName+' '+LName)
# print(len(FName+' '+LName))

##############################################################

# String = 'I am a intern in UST.\nI want to become the CEO of UST,\tThat is why I don\'t want studying so hard.'
# print(String)

###create a mult table###
# num = 2
# for i in range(1,10):
#     print (f"{num} * {i} = {num*i"})

########################################################################

# String = 'I am a intern in UST'
# print (String[0])
# for i in range (1,10):
#     print (String[i])

# length = len(String)*-1     ///*-1 for reverse purpuse
# for i in range (0,length):
#     print (String[i])

# for i in range (-1,length,-1):    //reverse
#     print (String[i])

# FirstThreeChar = String[0:3]
# print(FirstThreeChar)
# FirstThreeChar = String[::3]
# print(FirstThreeChar)
# FirstThreeChar = String[::-1]   //reverse
# print(FirstThreeChar)
# FirstThreeChar = String[3:]   
# print(FirstThreeChar)

# print(String.count('n'))    ///count the number of occurence
# print(String.count('UST'))

# print(String.endswith('intern'))    ///false 
# print(String.endswith('UST'))       ///True
# print(String.endswith(' '))        ///False

# print(String.expandtabs(10))        ///Increase the space of tab
# print(String)

# print(String.find('a'))   ///print index of first a from left
# print(String.rfind('a'))   ///print index of first a from right
# print(String.find('intern'))   ///print index of word intern (index of i)

####################################################################

# s = "Hello how are you doing after lunch"
# # x = s.index("are")     ///search particular word after the given index and return back the index
# y = s.index("a",7)
# z = s.index("you",5)
# # print(x)
# print(y)
# print(z)

######################################################################

# s = "hello how are you doing after lunch"
# a = "abcd34"
# b = "356"
# s2 = "3.4"
# s3 = "\u00b3"  #unsigned integer
# s4 = "XII"
# s5 = "10\u00b3"
# s6 = "10^2"
# s7 = "10\u00bd"
# print(s.isalnum())  ///false  (alphabet and number)
# print(a.isalnum())  ///true
# print(b.isalnum())  ///True
# print(a.isalpha())  ///false   (alphabets only)
# print(b.isdecimal())  ///true   ()
# print(s3.isdecimal())    ///false
# print(s3.isdigit())     ///true   ( if the string contains any one in [0-9],that is works with unsigned integer(unicode characters),not works on float)
# print(s3.isnumeric())       ///true
# print(s2.isdecimal())   ///False
# print(s2.isdigit())     ///false
# print(s2.isnumeric())     ///false  (true for numbers,unicode,roman letters)    
# print(s4.isdecimal())           ///false
# print(s4.isdigit())             ///false
# print(s4.isnumeric())           ///false
# print(s5.isdecimal())           ///false
# print(s5.isdigit())             ///true
# print(s5.isnumeric())           //true 
# print(s6.isdecimal())           ///false
# print(s6.isdigit())             ///True     
# print(s6.isnumeric())           ///true 
# print(s7.isdecimal())           ///false
# print(s7.isdigit())             ///false
# print(s7.isnumeric())           //true


# id = "e_29"
# print(id.isidentifier())   ///true if the string start with [a-z],[A-Z],_ and others should be[0-9] or _
# print(s.isidentifier())

# print(s.islower())        ///return true if all characters are lowercase

#########################################################################

a = ["hi","how","are","youa"]   
# print("?".join(a))              ////join using "?"

# b = (" ".join(a))       #///join using " 
# print(b.strip("ha"))       ///remove h from begning if present and a from end if present,that is strip from front and end   
# print(b.split(" "))         ///split the words 
# print(b.title())            /// make first letter of all words  in the string to uppercase
# print(b.swapcase())         ///all letter become uppercase
# print(a.replace("hi","hello"))
# print(a.startswith("hi"))

























