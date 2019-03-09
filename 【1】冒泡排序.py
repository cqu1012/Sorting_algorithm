# -*- coding: utf-8 -*-
#核心：两次for循环，每一个数字与后面数字分别比较
def sort(data):
    lenth = len(data)
    for  i in range(lenth):
        for j in range(lenth):
            if data[i] < data[j]:
                data[i],data[j] = data[j],data[i]
    return data

data = sort([2,1,4,13,11,12,10,6,4,7,8,3,2,12])
print(data)


