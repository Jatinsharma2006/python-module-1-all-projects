#step1:define fn using "def" keyword
def

#printing a string fn
def show():
    print("ONE PIECE is REAL")
show()#step 2 calling the fn

#designing a fn that takes some input(parameter)and gives some value(return type).
#campus question these are fn known as "pure funtions"{imp}

#intrest fn
def intrest(p,r,t):
    return p*r*t/100
i=intrest(1000,6,2)
print(i)

#square fn
def square(n):           #here(n)is a parameter
    return n*n          #return-used to transfer/give back result

a=square(5)
b=square(6)
print("A=",a,"b=",b)


#looping a user def fn
#USING LOOP TO PRINT MULTIPLE TIME

#1
def hello():
    print("ONE PIECE is BEST")

for i in range(1,11,1):
    show()

hello()

#2
def show():
    print("happy birthday lala")

for i in range(1,18+2):
    show()



