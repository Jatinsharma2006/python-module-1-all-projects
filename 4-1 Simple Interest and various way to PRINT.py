p=float(input("enter Principle"))
r=float(input("enter Rate"))
t=float(input("enter Time"))
#(p,r,t)=eval(input("Enter Principal,Rate,Time"))

si=(p*r*t/100)

               #various ways to print(\n means new line)#1

#print ('Interst=',si)
#print('Amount RS=',(p+si))

           
#print('Interst=',si,"\nAmount=",(p+si))


                       #print as in c#2

#print("interst=%f  \nAmount=%f"%(p, (p+si)))
#print("interst=%.2f  \nAmount=%.2f"%(p, (p+si)))


                       #using format fn

print("interst={} \nAmount={}".format(si,(p+si)))
#print("interst={:.2f} \nAmount={:.2f}".format(si,(p+si)))#point ke bade 2 value


                         #mordern way

#print(f'interst={si} \nAmount={p+si}')
 

print('ghacc students are best')
a=5
print(a)
print('I want',a ,'rs')
print('How much is %d '%a)
print(f'You are in {a}years')     












 
