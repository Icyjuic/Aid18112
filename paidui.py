L = [165,164,154,132,155,177,167,156,146,175]
l = len(L)
def fun(L,l):
    while l >1:
        flag = False
        for i in range(l-1):
            if L[i]>L[i+1]:
                L[i],L[i+1] = L[i+1],L[i]
                flag = True
        if flag==False:# 提前遍历结束
            return L
        l -=1
    return L
print(fun(L,l))
    
    xxxxx