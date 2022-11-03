
import array as myarray
array1 = myarray.array('i',[5,6,7,8])
array2 = myarray.array('d',[1.0,2.0,4.5])
array3 = myarray.array('u',['b','c','t','k'])
array1.sort()
print(array1)
#print(len(array1))



def sumup(givenarr):
    sum = 0
    h =0
    for j in range(len(givenarr)):
        sum = sum + givenarr[h]
        h = h + 1
    return sum
print(sumup(array2))
print(myarray.sort(array1))
