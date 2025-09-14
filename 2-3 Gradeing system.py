(e,h,m,s)=eval(input("enter e,h,m,s"))
total=e+h+m+s

percent=total/4
if percent>=80:
   grade="A"
elif percent>=70:
    grade="B"
elif percent>=40:
    grade="C"    
else:
    grade="D"
    
print(f"total={total} percent={percent} grade={grade}")
