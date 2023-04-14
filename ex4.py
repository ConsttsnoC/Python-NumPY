#свойства и представления массивов, создание их копий
import numpy as np
a = np.array([0.1,0.2,0.3])
print(a.dtype)
#float64
#преобразуем элемент без потери данных
a.dtype = np.int8()
print(a.dtype)
#int8
print(a.size)
#24 3*8
#проверка
a.dtype = np.float64()
print(a)

#чтобы узнать сколько памяти занимаем один элемент
print(a.itemsize)

#матрица из 1
b = np.ones((3,4,5))
print(b)
#чтобы узнать кол-во осей
print(b.ndim)
#чтобы узнать число элементов по каждой из оси
print(b.shape)
#так с помощью shape можно менять представление текущего массива
b.shape = 12, 5
print(b)

#чтобы присвоить копию представления view()
b = a.view()

#что бы создать копию
b = np.array( a )