s="III"
roman_integers={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
total=0
for i in range(len(s)-1):
    if roman_integers[s[i]]<roman_integers[s[i+1]]:
        total-=roman_integers[s[i]]
    else:
        total+=roman_integers[s[i]]
total+=roman_integers[s[i]]
print(total)
