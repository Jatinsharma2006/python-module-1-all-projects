#Reading data from file

filename=input("Enter Filename to Read")
try:
    f=open(filename,"r")
    lines=f.readlines()    #it will read all the lines as LIST[interview]
    for data in lines:
        print(data,end=" ")
        f.close()
except FileNotFoundError as ok:
    print("File Not Found",ok)
finally:
    print("bye")
