# This function will return revrsed digits
def rNum(n):
    s=int()
    while (n>0):
        s=s*10+n%10
        n=n//10
    return s
