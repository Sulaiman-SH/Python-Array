import array as ar

array1 = ar.array('i', [1, 2, 3, 4, 5, 6])
buffer = array1.buffer_info()
buffer2 = array1.buffer_info()[1]
print(buffer)
print(buffer2)
print(buffer2 * array1.itemsize)