def binary(value,key):
    left = 0
    right = len(value)-1
    
    while left <= right:
        middle = (left+right)//2
        if value[middle]==key:
            return middle
        elif value[middle]<key:
            left = middle +1
            continue
        elif value[middle]>key:
            right = middle-1
            continue
    return -1
l = [1,3,33,324,2412,124124,2424424,12312312,123123123]
k = 324
print(binary(l,k))