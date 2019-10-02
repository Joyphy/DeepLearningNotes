import numpy as np
#numpy 轴的概念axis
#轴可以从空间维度上理解,及选取哪个轴,即在这个轴的方向上进行操作,由于各个方向独立,所以这只影响该方向本身,其他轴没有变化
#如果从numpy中的数字来体现则更为直接一点,选取哪个轴操作,只有那个轴上的数字会发生变化

z1 = np.arange(2520).reshape(3,4,5,6,7)
print(z1.max(axis = 0).shape)
#结果为(4, 5, 6, 7),可以看成(1,4,5,6,7)
print(z1.max(axis = 2).shape)
#结果为(3, 4, 6, 7),可以看成(3,4,1,6,7)
#max,sum,min,mean属于降维操作,故该轴只剩1,numpy自动省略

z2 = np.ones((3,4,5,1,7))
z = np.concatenate((z1, z2), axis = 3)
print(z.shape)
#结果为(3, 4, 5, 7, 7),concatenate属于升维操作,故该轴数字相加

#numpy 数组拼接
a1 = np.ones((3,4))
a = np.append(a1,5)
print(a)
#结果为[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 5.],会把前一个数组压平

a2 = np.zeros((3,4))
a = np.append(a1, a2)
print(a)
#结果为[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.],不指定轴也会把前一个数组压平

a = np.append(a1, a2, axis = 0)
print(a.shape)
#结果为(6,4)

a = np.append(a1, a2, axis = 1)
print(a.shape)
#结果为(3,8)

#专业拼接方法concatenate
a3 = np.full((5,4), 2)
a = np.concatenate((a1,a2,a3),axis = 0)
print(a.shape)
#结果为(11,4)

#insert, 第一个参数为array,第二个参数为索引,第三个参数为插入值,总体来讲不好用
b = np.insert(a1, 5, 8)
print(b)
#结果为[1. 1. 1. 1. 1. 8. 1. 1. 1. 1. 1. 1. 1.]

a4 = np.full((3,2), 8)
b = np.insert(a1, [2, 3], a4, axis = 1)
print(b)
'''结果为
[[1. 1. 8. 1. 1.]
 [1. 1. 8. 1. 1.]
 [1. 1. 8. 1. 1.]]
 '''

a5 = np.full((1,4), 8)
b = np.insert(a1, [2], a5, axis = 0)
print(b)
'''结果与上面一样
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [8. 8. 8. 8.]
 [1. 1. 1. 1.]]
 '''
b = np.insert(a1, 2, a5, axis = 0)
print(b)
'''结果与上面一样
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [8. 8. 8. 8.]
 [1. 1. 1. 1.]]
 '''

b = a1.flatten()
b = np.insert(b, [2, 3, 7], [5, 6, 8])
print(b)
#连续插入数值,按照从右到左的顺序依次插入

#hstack, vstack不说了这里

#delete函数
a6 = np.arange(20).reshape(4,5)
c = np.delete(a6, 5)
print(c)
#结果为[ 0  1  2  3  4  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

c = np.delete(a6, [3], axis = 1)
print(c)
'''
[[ 0  1  2  4]
 [ 5  6  7  9]
 [10 11 12 14]
 [15 16 17 19]]
 '''

c = np.delete(a6, [1, 3], axis = 0)
print(c)
'''
[[ 0  1  2  3  4]
 [10 11 12 13 14]]
 '''
