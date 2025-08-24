n=19
ans=n
seen=set()
while ans!=1:
    if ans in seen:
        print("False")
    seen.add(ans)
    total=0
    for i in str(ans):
        total+=int(i)**2
    ans=total
else:
    print("true")
