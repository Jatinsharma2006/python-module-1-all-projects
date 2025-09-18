#cannot be overwitten
filename=input("Enter Filename to Create")
try:
    f=open(filename,"w")
    print("Type Text or by Bye to stop:")
    while True:
        data=input()
        if data=="Bye": break
        f.write(data+"\n")
    f.close()
    print("File created")
except Exception as e:
    print("Exception Occured",e)
finally:
    print("Ghacc")
#to overwrite write "a" insted of "w"        
  
