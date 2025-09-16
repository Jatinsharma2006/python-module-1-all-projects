#name argument fn
def intrest(p,r,t):
    return p*r*t/100

def main():
    a=intrest(5000,5,3)
    #without namee first value=p second=r third=t
    b=intrest(p=10000,t=6.25,r=1)
    c=intrest(t=10,r=15,p=1000)#named argument 
    print(f"interest={a}  interest={b}  interest={c}")
   
    

main()
