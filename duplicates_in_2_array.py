
def binarysearch(arr1 ,elem ,low ,high):
    if (low > high ):
        return None
    mid = int((low + high) / 2)
    if( elem == arr1[mid]):
        return elem
    elif (elem < arr1[mid]):
        return binarysearch(arr1,elem, low, mid-1)
    elif(elem > arr1[mid]):
        return binarysearch(arr1,elem, mid+1, high)


arr1 = [4,2,7,1,3 ]
arr2 = [3,4,5,6,7,8 ]
arr1. sort()
arr2.sort()

# Iterate through array2 to check if element is present
for i in range(len(arr2)):
    ret = binarysearch(arr1,arr2[i],0 ,len( arr1) -1)
    if ( ret != None):
        print(arr2[i])





