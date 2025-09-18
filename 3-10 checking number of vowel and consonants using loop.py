                        #karab wAALA TARIKA LENTHY PROCESS

"""
name=input("Enter a name(string)")
vowel=0
consonants=0
i=0
n=len(name)

while i<n:
    if name[i]=="a" or name[i]=="e" or name[i]=="i"or name[i]=="o" \
       or name[i]=="u":
        vowel=vowel+1
    else:
        consonants=consonants+1
    i=i+1
print("vowels=",vowel,"consonants=",consonants)
"""

name=input("Enter a name(string)")
(vowel,consonants)=(0,0)
for k in name:
    if k     in "aeiouAEIOU":
        vowel+=1
    else:
        consonants+=1
print(f"vowel={vowel} consonants={consonants}")

 











