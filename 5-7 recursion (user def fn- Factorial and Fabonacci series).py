#factorial
"""
def factorial(n):
    if n<1:
        return 1
    else:
        return n*factorial(n-1)
    
def main():
    n=int(input("Enter a number"))
    m=factorial(n)
    print("result=",m)
main()
"""
#fabnacci series
def fabnacci(n):
    if n==0 or n==1:
            return n
    elif n>=2:
        return fabnacci(n-2)+fabnacci(n-1)

def main():
    m=int(input("enter number of terms to print:"))
    for n in range(0,m):
          print(fabnacci(n),end="\t")
main()














    
