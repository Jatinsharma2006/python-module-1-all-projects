Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
txt="hello world"
print(txt.find("l"))
2
a="hello ,world welcome to my world!"
print(txt.find("e"))
1
print(txt.find("x"))
-1
print(a.find("e"))
1
print(a.find("d"))

11
print(a.find("o",12,23))
17
print(a.rfind("w"))
27
a="hello ,world welcome to my world!"
print(a.index("d"))
11
print(a.rindex("o"))
28
txt="my name is {fname},i am {age}".format(fname="john",age="36'")
print(txt)
my name is john,i am 36'
txt="my name is {1},i am {0}".format("john","36'")
print(txt)
my name is 36',i am john
txt="my name is {},i am {}".format("john","36'")
print(txt)
my name is john,i am 36'
txt="i could eat bananas all day"
print(txt.partition("bananas"))
('i could eat ', 'bananas', ' all day')
print(txt.partition("apple"))
('i could eat bananas all day', '', '')
txt="i could eat bananas bananas bananas bananas all day"
print(txt.partition("bananas"))
('i could eat ', 'bananas', ' bananas bananas bananas all day')
print(txt.rpartition("bananas"))
('i could eat bananas bananas bananas ', 'bananas', ' all day')
>>> a="hello ,world welcome to my world!"
>>> print(a.index("world"))
7
>>> print(a.index("welcome"))
13
>>> print(a.rindex("world"))
27
>>> print(a.rindex("welcome"))
13
>>> print(a.index("r",5,11))
9
>>> print(a.find("r",5,11))
9
