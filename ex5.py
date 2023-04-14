#изменения формы массивов, добавление и удаление осей
import numpy as np
#создаем одномерный массив
a = np.arange(10)
print(a)
#изменяем форму одномерного в двумерный массив
a.shape = 2,5
print(a)
#присваиваем представление двумерного обратно в одномерный
b = a.reshape(10)
print(b)

#операция по изменению числа элементов и формы миссива, было 10 элементов, стало 9
a.resize(3,3,refcheck=False)
print(a)

#трансонирование матрицы векторов, замена строк на столбцы
a = np.array([(1,2,3),(4,5,6),(7,8,9)])
print(a)
b = a.T
print(b)

#добавление и удаление осей
x_test = np.arange(32).reshape(8,2,2)
print(x_test)
print(x_test.shape)
#добавляем новую ось
x_test4 = np.expand_dims(x_test,axis=0) #вторый пареметром указываем какую ось хотим добавить
print(x_test4.shape)
#удаление оси
a = np.append(x_test4,x_test4,axis=0) #0 первая ось -1 последняя ось
print(a.shape)
b = np.delete(a,0,axis=0)
print(b.shape)

#удаление из массива оси, где всего 1 элемент
с = np.squeeze

#добавление новой оси
a = np.arange(10)
b = a[np.newaxis, :]
print(b.shape)
