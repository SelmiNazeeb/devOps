import os
print("current directory",os.getcwd())
try:
    f = open("file1.py")
    #print(f.read())
    #print(f.readline())     #single line
    #print(f.readlines())    #multiple lines
    print(type(f.readlines()))  #output - <class 'list'>
    print(type(f.readline()))   #output - <class 'str'>
    os.remove("file10.txt")     #remove the file
    os.remove(f'C:\\Users\\shell\\new.txt')   #remove the file
except:
    print("file not found")
finally:
    f.close()