# 顺序查找

# 原始数据 [3,2,1,4,6,5,8,7,9,13,12,11,10]

def linnear(value, key):
    # 使用下标遍历所有数据
    for i in range(len(value)):
        if value[i] == key:
            # 对比当前数据与待查找值
            print('找到了')
            return i
    # 遍历完所有数据仍未找到时
    else:
        # 查找失败
        return -1

if __name__ == "__main__":
    # 原始数据
    value = [3,2,1,4,6,5,8,7,9,13,12,11,10]
    # 待查找值
    key = 6

    # 顺序查找
    res = linnear(value,key)
    if res == -1:
        print('查找失败')
    else:
        print('查找成功,对应下标值:',res)