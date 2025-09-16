"""
#passing arguments to fn using list unpacking
def intrest(p,r,t):
    return p*r*t/100

def main():
    data=[10000,6.25,1]   #list  
    a=intrest(*data)      #list is getting unpack
    print(f"interest={a}")


main()
"""

def OKK(*names):
    for n in names:
        print(n,end="\t")


def main():
    OKK(["ranchoo","faran","raju"])
    OKK("rancho","faran","raju","chatur","priya","\n")

main()    
#passing arguments to fn using dictionary unpacking

def intrest(p,r,t):
    return p*r*t/100

def main():
    data={"p":10000,"t":3,"r":6.25}   #dictionary 
    a=intrest(**data)      #dictionary is getting unpack we use one * for list and two for dictionary

    print(f"interest={a} ")


main()
