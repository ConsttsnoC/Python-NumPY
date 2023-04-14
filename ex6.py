#объединение и разделение массивов
import numpy as np
#a = np.array([(1,2),(3,4)])
#b = np.array([(5,6),(7,8)])
#print(a)
#print(b)

#объединяет массивы по горизонтали
#print(np.hstack([a,b]))

#объединяет массивы по горизонтали по вертикали
#print(np.vstack([a,b]))


#объединение двух векторов
#print(np.column_stack([a,b]))


#многомерный массив, объединения по любой оси
#a = np.arange(1,13)
#b = np.arange(13,26)
#a.resize(3,3,2)
#b.resize(3,3,2)
#print(a)
#print(b)

#c0 = np.concatenate([a,b], axis=0) #объединение по 1 оси

#объединение с помощью r_ и c_
#print(np.r_[[1,2,3],4,5])
#print(np.c_[[(1,2,3),(4,5,6)],[[7],[8]]])

#РАЗДЕЛЕНИЕ МАССИВОВ
a = np.arange(10)
#по горизонтали
print(np.hsplit(a,2))
#по вертикали
a.shape = 10, -1
print(np.vsplit(a,2))