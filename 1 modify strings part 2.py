
a="hello world"
print(a.replace("l","j"))
hejjo worjd


txt="i like bananas"
print(txt.replace("bananas","apple"))
i like apple


text="one one one one one one"
print(text.replace("one","two",4))
two two two two one one


txt="banana"
print(txt.center(20))
       banana

       
print(txt.center(20,"o"))
ooooooobananaooooooo


print(txt.center(20,"z"))
zzzzzzzbananazzzzzzz


txt="banana"
print(txt.ljust(20))
banana


print(txt.ljust(20,"z"))
bananazzzzzzzzzzzzzz


print(txt.rjust(20,"z"))
zzzzzzzzzzzzzzbanana


print(txt.zfill(30))
000000000000000000000000banana


txt="h\tl\te\tl\tl\to"
print(txt)
h	l	e	l	l	o



print(txt.expandtabs(5))
h    l    e    l    l    o


print(txt.expandtabs(20))
h                   l                   e                   l                 l                   o


>>> print(txt.expandtabs(2))
h l e l l o


>>> txt="i like apples,apples are my favourit fruit.do you like apples"
>>> print(txt.count("apples"))
3
>>> print(txt.count("apples",10,24))
1
>>> print(txt.count("apples",10))
2
