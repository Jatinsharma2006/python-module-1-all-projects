try:
    (d,t)=eval(input('enter Displacement,Time:'))
    v=d/t
    print('Velocitity=',v,"ms")

except ZeroDivisionError as ok:
    print("Sorry,Time Cannot be Zero")
except NameError as ko:
    print("Invalid Number",ko)
finally:
    print('Thanks/Reached to Panchmadi')      
