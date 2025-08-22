s="   fly me   to   the moon  "
r=-1
temp=""
while s[r]==" ":
    r-=1
while r>=-len(s) and s[r]!=" ":
    temp+=s[r]
    r-=1
print(len(temp))
