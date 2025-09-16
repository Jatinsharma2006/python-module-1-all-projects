x="me hu naa"
def hello():
    global x
    x="tum ho naa"
    print(x)
hello()
print(x)

#without global keyword
a=1                              #global scope
def change():
    a=2                          #local scope
    print("a inside the fn is",a)
def main():
    print("\nFinal value of a is ",a)
main()
#with global keyword
a=1                              #global scope
def change():
    global a
    a=2                          #local scope
    print("a inside the fn is",a)
def main():
    print("\nFinal value of a is ",a)
main() 
