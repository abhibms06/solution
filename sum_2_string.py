# Perform sum of 2 numbers

value1 = input()
value2 = input()

def sum(s1,s2):
    i = len(s1) - 1
    j = len(s2) - 1
    print('Inside sum func')

    result = ''
    final_value = ''
    while i >=0 or j >= 0:
        tmp1 = tmp2 = 0
        if i >= 0:
            tmp1 = s1[i]
        if j >= 0:
            tmp2 = s2[j]

        if len(result) == 0:
            result = '0'

        result = str(int(tmp1) + int(tmp2) + int(result[0]) )

        if len(result) > 1:
            final_value = result[1] + final_value
        else:
            final_value = result + final_value
            result = ''

        i = i - 1
        j = j - 1


    if len(result) > 1:
        final_value = result[0] + final_value

    return final_value

print(sum(value1,value2))
