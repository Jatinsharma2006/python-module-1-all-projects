#calculating sum and avg of any number of value passed to the fn (Interview/EQ)


def summation(*args):
    s=0               #identity value for+
    for value in args:
        s+=value      #or s=s+ value
    return(s,s/len(args))                    #returning multiple values
    #return(sum and avg)
def main():
    (s1,a1)=summation(10,20,30)
    (s2,a2)=summation(5,1,4,3,10)
    print(f"result1={s1},{a1}        Result2={s2},{a2}")
main()

def summation(*ok):
    s=0               #identity value for+
    for value in ok:
        s+=value      #or s=s+ value
    return(s,s/len(ok))                    #returning multiple values
    #return(sum and avg)
def main():
    (s1,a1)=summation(10,20,30)
    (s2,a2)=summation(5,1,4,3,10)
    print(f"result1={s1},{a1}        Result2={s2},{a2}")
main()


  
