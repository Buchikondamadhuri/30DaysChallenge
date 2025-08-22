def isPalindrome(x):
        if x<0:
            return False
        return str(x)==str(x)[::-1]
        '''x1=str(x)
        l=0
        r=len(x1)-1
        while l<r:
            if x1[l]!=x1[r]:
                return False
            l+=1
            r-=1
        return True'''
x=-121
print(isPalindrome(x))