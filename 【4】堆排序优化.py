# -*- coding: utf-8 -*-
from math import floor

'''
堆排序：
节点i的左节点为i*2+1   [条件：i*2+1<len(data)]
节点i的右节点为i*2+2   [条件：i*2+2<len(data)]
节点i的父节点为floor((i-1)//2)     [条件：i>0]

核心：利用二叉树性质遍历列表，转化成二叉树排序，
在分别取出第一个值放入列表中，对剩余列表继续执
行二叉树排序，重复以上，当列表中只剩下一个值时，
堆排序完成。
'''

#父节点
def parent(i):
    return floor((i-1)//2)
#左节点
def left(i):
    return i*2+1
#右节点：
def right(i):
    return i*2+2
def judge_parent(i,data):
    '''
    :param i: 当前节点
    :param data: 当前列表
    :return: 排序完成后列表
    '''
    j = i
    while parent(j) >= 0:
        if data[parent(j)] > data[j]:
            data[parent(j)], data[j] = data[j], data[parent(j)]
            j = parent(j)
        else:
            j = -1
    return data


#二叉树排序
def binay_tree(data):
    lenth = len(data)
    for i in range(lenth):
        if lenth > 0 :
            if left(i) < lenth:
                if data[i] > data[left(i)]:
                    data[i],data[left(i)] = data[left(i)],data[i]
                    judge_parent(i, data)
                else:
                    if right(i) < lenth:
                        if data[i] > data[right(i)]:
                            data[i],data[right(i)] = data[right(i)],data[i]
                            judge_parent(i, data)
    return data

#调用二叉树排序，使之为堆排序
data_f = []
def pileSort(data):
    if len(data)>1:
        data_1 =  binay_tree(data)
        data_f.append(data_1[0])
        data_1.remove(data_1[0])
        pileSort(data_1)
    return data_f+data

if __name__ == '__main__':
    data = [2, 1, 4, 13, 11, 12, 10, 6, 4, 7, 8, 3, 2, 12]
    # data =  [-1, -1, 0, 0, 0, 12, 22, 3, 5, 4, 3, 1, 6, 9]
    print('排序前：',data)
    print('二叉树排序：',binay_tree(data))
    print( '堆排序：',pileSort(data))



