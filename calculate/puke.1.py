# 顺序查找

# 原始数据 [1,22,234,333,424,523,566,644,645,677,788,799,900]
# 查找677


value = [1,22,234,333,424,523,566,644,645,677,788,799,900]
left = 0
right = len(value)-1
key = 677
def binary(value, key, left, right):
    # 退出条件
    if left > right:
        # 查找失败
        return -1
    # 获取中间元素，对应下标值
    middle = (left+right)//2

    # 对比中间元素值与指定查找值
    if value[middle] == key:
        # 查找成功
        return middle
    elif value[middle] > key:
        # 则在左侧继续查找
        right = middle-1
        return binary(value,key,left,right)

    elif value[middle] < key:
        # 则在右侧继续查找
        left = middle+1
        return binary(value,key,left,right)

print(binary(value, key, left, right))

        