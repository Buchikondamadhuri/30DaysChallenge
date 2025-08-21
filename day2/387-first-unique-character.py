def firstUniqueCharacter(s):
    dici={}
    for i in s:
        if i not in dici:
           dici[i]=1
        else:
           dici[i]+=1
    for i in range(len(s)):
        if dici[s[i]]==1:
            return i
    return -1
s="leetcode"
print(firstUniqueCharacter(s))