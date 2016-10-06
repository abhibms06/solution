# One away: There are 3 types of edits that can be performed on strings: One replace or one delete or one insert a character
# Given 2 strings write a function to check if they are one edit(0 edits away)



def check_edits(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    value = True

    # Make sure length of s1 is bigger than s2

    if l1 < l2:
        s1,s2 = s2,s1
        l1,l2 = l2,l1

    i = 0
    no_of_edit = 0
    while i < l2 and value == True:

        if s1[i] == s2[i]:
            i = i + 1
        else:
            s2 = s2[0:i] + s1[i] + s2[i:]
            no_of_edit = no_of_edit + 1
            l2 = len(s2)

            if no_of_edit > 1:
                value = False

    if abs(l1 - l2) > 1:
        value = False

    return value


s1 = 'pale'
s2 = 'pale'
print(check_edits(s1,s2))


