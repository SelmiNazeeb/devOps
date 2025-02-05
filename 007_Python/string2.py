s1 = "devops"
s2 = "batch"
s3 = "2"
s = s1+" "+s2+" " +s3   #concatination
print(s)
print(len(s))
print(s.upper().find("V"))   #make uppercase and find index of "V"
print(s[0:6])          #print devops only
print(s.split()[0])    #print devops only
print(s.split()[1])    #print batch only
print(s[len(s)-1])     #print last index
print(s.index(s[-1]))  #find last index of string
print(s.index("b"))