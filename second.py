def f(k1,k2,x):
    if (k1+k2) >= 82 and x==4:
        return 1
    if ((k1+k2) >= 82 and x!=4) or ((k1+k2) < 82 and x == 4):
        return 0
    else:
        if x % 2 != 0:
            return f(k1+1,k2,x+1) or f(k1*4,k2,x+1) or f(k1,k2+1,x+1) or f(k1,k2*4,x+1)
        else:
            return f(k1+1,k2,x+1) and f(k1*4,k2,x+1) and f(k1,k2+1,x+1) and f(k1,k2*4,x+1)
for k2 in range(1,78):
    if f(4,k2,1):
        print(k2)