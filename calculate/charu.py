# 练习：
# 下午2：00下课，幼儿园小孩放学，秦老师直到小朋友做游戏，按照插入排序的规则，
# 组织小朋友按身高从低到高排成一排，使用Python代码实现该过程。

# L = [30,70,30,50,69,80]
G = [44,1,323,24,2424,333,88,123]
def fun(L):
    L1 = [L[0]]
    print(L1)
    L2 = L[1:]
    print(L2)
    k = 1
    for i in L2:
        L1.append(L1[-1])
        for j in range(-2,-(k+2),-1):
            if i >= L1[j]:
                L1[j+1]=i
                break
            elif i < L1[j]:
                L1[j+1] = L1[j]
                L1[j] = i

        print(L1)
        k+=1
    
    return L1

fun(G)