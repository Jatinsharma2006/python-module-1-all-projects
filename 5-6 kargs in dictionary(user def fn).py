#sometimes we need to pass both key:value to the fn(insted of list).
#here we use" **kargs " to represent unknown no. of dictionary items.
#ex passing name and hobby of student to the fn


def show(kargs):            #define fn
    for(name,hobby) in kargs.items():
        print(f"hobby of  {name}  is {hobby}")
def main():
        data={"rancho":"experiment","farhan":"photography","raju":"drawing"}
        show(data)           #step II:calling fn

main()   
#passing   unknow number of "named args"to the fn.

def data(**kargs):            
    for(key,value) in kargs.items():
        print(f"{key}=>{value}")
def main():
        data(name="rancho",age=20,hobby="Research",fullname="rancho chandad",ranking=1)

main()                

