# -*- coding: utf-8 -*-
'''

'''
def bin_search(data,val):
    '''
    :param data:传入的数组
    :param val: 需要查找的值
    :return: 是否查找成功
    '''
    low = 0
    high = len(data)-1
    while low < high:
        mid = (high - low)//2
        if data[mid] == val:
            return True
        elif data[mid] < val:
            low += 1
        elif data[mid] > val:
            high -= 1
    return False

if __name__ == '__main__':
    data = [2, 1, 4, 13, 11, 12, 10, 6, 4, 7, 8, 3, 2, 12]
    print(bin_search(data,17))





