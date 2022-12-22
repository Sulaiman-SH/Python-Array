import array as ar

array1 = ar.array('i', [1, 2, 3, 4])
print('before extend', array1)
exte = array1.extend(array1)
print('after extend', array1)