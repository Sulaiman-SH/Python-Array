import array as ar

array1 = ar.array('i', [1, 3, 5, 7, 9])
print('before remove: ', array1)
array1.remove(5)
print(array1)