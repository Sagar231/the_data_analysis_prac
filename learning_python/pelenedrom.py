def ispelen(s):
    i = 0             
    j = len(s)-1
    while(i<=j):
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True
print(ispelen("123321"))
print(ispelen("12331"))