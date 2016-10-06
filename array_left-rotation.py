

def array_left_rotation(a, n, k):
    for i in range(k):
        a.append(a.pop(0))

    return a

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
for i in answer:
    print(i, end=' ')
