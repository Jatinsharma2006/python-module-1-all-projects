>>> b="hello ,world!"
>>> print(b[2:7])
llo ,
>>> print(b[:7])
hello ,
>>> print(b[2:])
llo ,world!
>>> print(b[-7:-2])
,worl
>>> print(len(b))
13
>>> a=b.upper()
>>> a
'HELLO ,WORLD!'


>>> a.lower()
'hello ,world!'


a.casefold()
'hello ,world!'


a.capitalize()
'Hello ,world!'

c="PYTHON IS FUN"
c.capitalize()
'Python is fun'


d="Hello WORld"
d.swapcase()
'hELLO worLD'


txt=",,,,...,,rrtrtrtgtrgtr..r.rrrttbanana.,.,...rrhello..,.,"
x=txt.strip("g.,rtrl")
print(x)
banana.,.,...rrhello



a="   hello, world    "
print(a.strip())
hello, world


x=txt.lstrip("g.,rtrl")
print(x)
banana.,.,...rrhello..,.,


print(txt.rstrip("g.,rtrl"))
,,,,...,,rrtrtrtgtrgtr..r.rrrttbanana.,.,...rrhello


a="hello,world"
print(a.split(","))
['hello', 'world']


r="hellorwinriram"
print(r.split("r"))
['hello', 'win', 'i', 'am']



txt="apple#banana#orange#cherry#red#blue#yellow"
x=txt.split("#",4)
print(x)
['apple', 'banana', 'orange', 'cherry', 'red#blue#yellow']



txt="apple#banana#orange#cherry#red#blue#yellow"
x=txt.rsplit("#",4)
print(x)
['apple#banana#orange', 'cherry', 'red', 'blue', 'yellow']




txt="thank you for the music\nwelcome to the jungle"
print(txt.splitlines())
['thank you for the music', 'welcome to the jungle']




