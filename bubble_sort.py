# https://www.hackerrank.com/challenges/30-sorting

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

number_of_swaps = 0
for i in range(len(a)):
    for j in range(len(a)-1-i):
        if (a[j] > a[j+1]):
            a[j],a[j+1] = a[j+1],a[j]
            number_of_swaps = number_of_swaps + 1

print(a)
print('Array is sorted in', number_of_swaps ,'swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])