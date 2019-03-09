# -*- coding: utf-8 -*-
from math import floor

'''
堆排序：
节点i的左节点为i*2+1   [条件：i*2+1<len(data)]
节点i的右节点为i*2+2   [条件：i*2+2<len(data)]
节点i的父节点为floor((i-1)//2)     [条件：i>0]
'''
#父节点
def parent(i):
    # print('i:',floor((i-1)//2))
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
    :param data: 列表
    :return: 是否有父结点
    '''
    pass

def binay_tree(data):
    lenth = len(data)
    for i in range(lenth):
        print('i:{}'.format(i))
        if lenth > 0 :
            j = i
            while parent(j) >= 0:
                if data[parent(j)] > data[j]:
                    print('1.此时交换data{}：{}，父节点data{}：{}'.format(j,data[j],parent(j),data[parent(j)]))
                    data[parent(j)], data[j] = data[j], data[parent(j)]
                    print(data)
                    #当当前节点与父节点交换后还存在父节点
                    j = parent(j)
                else:
                    j = -1
            else:
                if left(i) < lenth:
                    if data[i] > data[left(i)]:
                        print('2.此时交换data{}：{}，左节点data{}：{}'.format(i, data[i], left(i), data[left(i)]))
                        data[i],data[left(i)] = data[left(i)],data[i]
                        print(data)
                        j = i
                        while parent(j) >= 0:
                            if data[parent(j)] > data[j]:
                                print('1.此时交换data{}：{}，父节点data{}：{}'.format(j, data[j], parent(j), data[parent(j)]))
                                data[parent(j)], data[j] = data[j], data[parent(j)]
                                print(data)
                                # 当当前节点与父节点交换后还存在父节点
                                j = parent(j)
                            else:
                                j = -1
                    else:
                        if right(i) < lenth:
                            if data[i] > data[right(i)]:
                                print('4.此时交换data{}：{}，右节点data{}：{}'.format(i, data[i], right(i), data[right(i)]))
                                data[i],data[right(i)] = data[right(i)],data[i]
                                print(data)
                                j = i
                                while parent(j) >= 0:
                                    if data[parent(j)] > data[j]:
                                        print('1.此时交换data{}：{}，父节点data{}：{}'.format(j, data[j], parent(j), data[parent(j)]))
                                        data[parent(j)], data[j] = data[j], data[parent(j)]
                                        print(data)
                                        # 当当前节点与父节点交换后还存在父节点
                                        j = parent(j)
                                    else:
                                        j = -1
    return data

#调用二叉树排序，使之为堆排序
data_f = []
def pileSort(data):
    if len(data)>1:
        data_1 =  binay_tree(data)
        data_f.append(data_1[0])
        data_1.remove(data_1[0])
        pileSort(data_1)
    return data_f


if __name__ == '__main__':
    # data = [2, 1, 4, 13, 11, 12, 10, 6, 4, 7, 8, 3, 2, 12]
    data =  [-1, -1, 0, 0, 0, 12, 22, 3, 5, 4, 3, 1, 6, 9]
    print( pileSort(data))



