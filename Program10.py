import array as ar

array1 = ar.array('i', [1, 2,3 ,4 , 5, 6])
print('before insert: ', array1)
array1.insert(1,10)
print('after insert: ',array1)