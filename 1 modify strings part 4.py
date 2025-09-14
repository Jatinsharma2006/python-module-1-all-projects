Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
txt="hi sam!"
x="msa"
y="yjo"
mytable=str.maketrans(x,y)
print(txt.translate(mytable))
hi joy!
txt="hello sam!"
x="lams"
y="oejr"
z="he"
alpha=str.maketrans(x,y,z)
print(txt.translate(alpha))
ooo rej!
txt="hello ,welcome to my world."
print(txt.startswith("hello"))
True
print(txt.startswith("h"))
True
print(txt.startswith("hi"))
False
print(txt.startswith("hello ,mehuone"))
False
print(txt.endswith("my world"))
False
print(txt.endswith("my world."))
True
x="company"

print(x.isalnum())
True
x="com pany"
print(x.isalnum())
False
x="c2301ompany"

print(x.isalnum())
True
x="com_pany"
print(x.isalnum())
False
x="company"
print(x.isalpha())
True
x="c2301ompany"
print(x.isalpha())
False
print(x.isascii())
True
y="104 101 108 108 111"
print(y.isascii())
True
print(y.isdecimal())
False
y="4903"
print(y.isdecimal())
True
y="49.03"
print(y.isdecimal())
False
r="hello!\nhow are you"
print(r.isprintable())

False
r="hello!\thow are you"
print(r.isprintable())
False
v="hi"
j=35
r="hello!{v}how are{j} you"
>>> r=f"hello!{v}how are{j} you"
>>> print(r.isprintable())
True
>>> r
'hello!hihow are35 you'
