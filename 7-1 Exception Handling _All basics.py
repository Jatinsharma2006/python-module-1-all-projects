#Exception Handling

#This will Raise an exception because x is not defined
try:
    print(x)
except:    
    print("An Exception Occured")

#defing x
x=3
try:
    print(x)
except:    
    print("An Exception Occured")



#Executing special block of code for a special kind of error
try:
    print(x)
except NameError:    #Execute only if NameError Occur
    print("Variable x is not defined")
except:    
    print("Something else went wrong")



#Else block of code will be executed if their is no error while executing try part
try:
    print("Hello")
except:    
    print("Something else went wrong")
else:
    print("Nothing is wrong")



#finally:execute no matter what happen
#before defing x
try:
    print(x)
except:    
    print("Something else went wrong")
finally:
    print("The 'try-except' is finished")
#After defing x
x=3
try:
    print(x)
except:    
    print("Something else went wrong")
finally:
    print("The 'try-except' is finished")



#Raise
#raise a error if x is lower than zero
x=-1
if x<0:
    raise Exception("Sorry, no number below zero")

#can specify what kind of error to raise
x="Hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")




    
