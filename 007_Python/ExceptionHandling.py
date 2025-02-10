try:
    #print(10+50)    #output - 60
    #print(10+'50')  #output - something went wrong
    #print(10/0)    #zeroDivision error
    print(int("5+z"))  #value error
except TypeError:
    print("something went wrong")
except ValueError:
    print("This is a value error")
except ZeroDivisionError:
    print("This is a zero division error")
finally:
    print("success")