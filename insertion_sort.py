# Insertion sort

arr = [100, 45, 23, 12, 43, 33, 90]

print("Array : ",arr)

for i in range(len(arr)):
    if i == 0:
        continue

    elem = arr[i]
    j = i - 1
    while elem < arr[j] and j >= 0:

        arr[j+1],arr[j] = arr[j],arr[j+1]

        j = j -1


print("Sorted : ",arr)
