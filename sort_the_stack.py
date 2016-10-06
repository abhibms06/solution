# Sort the stack such that smallest elements are at top.
# You can use temp stack

def sort_stack_from_smallest_largest(s1):
    s2 = []

    while len(s1) > 0:
        elem = s1.pop()

        index = len(s2) - 1
        n = 0
        while index >= 0 and elem < s2[index]:
            index = index - 1
            n = n + 1

        # remove items from s2 and insert to s1
        for i in range(n):
            s1.append(s2.pop())

        s2.append(elem)

    # insert all s2 elements to s1 stack
    while len(s2) > 0:
        s1.append(s2.pop())

    return s1

# main() program
s1 = [int(i) for i in input().split()]
#print(s1)

print(sort_stack_from_smallest_largest(s1))
