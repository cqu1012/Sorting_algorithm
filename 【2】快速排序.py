# -*- coding: utf-8 -*-
'''
核心：利用递归的思想，对数组中取出（remove）一个数字，
作为中间数，比它小的放右边数组，比他大的放左边数组,在对
左边右边数组分别在做此方法，知道数组长度等于1.
'''

def quick_sort(data):
    if len(data) > 1:
        left,right = [],[]
        mid = data[len(data)//2]
        data.remove(mid)
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left)+[mid]+quick_sort(right)
    else:
        return data

data = [2,1,4,13,11,12,10,6,4,7,8,3,2,12]
print(quick_sort(data))
