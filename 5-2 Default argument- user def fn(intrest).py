#default argument
def intrest(p,r=8,t=3):
    return p*r*t/100

print(intrest(8000,6,2))
#default value 
print(intrest(5000,9))
print(intrest(3000))
print(intrest(1000,t=5))
# will give error for missing positinal arument p
print(intrest(r=4,t=6))


#input values by user in one line
def intrest(p,r,t):
    return p*r*t/100

def main():
    (p,r,t)=eval(input("Principle Rate Time"))
    a=intrest(p,r,t)
    print(f"interest={a}")

main()
