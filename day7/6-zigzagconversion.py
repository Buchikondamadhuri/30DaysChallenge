s="PAYPALISHIRING"
numRows=4
rows=["" for i in range(numRows)]
curr_row=0
step=1
for i in s:
    rows[curr_row]+=i
    if curr_row==0:
        step=1
    elif curr_row==numRows-1:
        step=-1
    curr_row+=step
if numRows==1:
    print(s)
else:
    print("".join(rows))