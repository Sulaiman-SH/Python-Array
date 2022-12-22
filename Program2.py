import array as ar

array1 = ar.array('i', [1, 2, 3, 4, 5])
print('Before the append: ', array1, '\n')
array1.append(119999999)
print('after the append: ', array1)