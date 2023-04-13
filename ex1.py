import numpy as np

#однородный многомерный массив
a = np.array([1,2,3,4,5,6,7,8,9])
#уберет из масиива False
a[[True,True,True,True,True,True,True,True,False]]
#создаст двумерный массив из элеменов a
b = a.reshape(3,3)
#обращение к элементам двумерного массива
b[1,2]