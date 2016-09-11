# Find max length substring in a given string

print('Enter a string : ')
string = input().strip()

# Get number of occurrence of each character from string
no_of_char_occur = {}
for i in range(len(string)):
    value = no_of_char_occur.get(string[i].lower())
    if value == None:
        no_of_char_occur[string[i].lower()] = 1
    else:
        no_of_char_occur[string[i]] = value + 1


# Display number of occurrence
#for key in no_of_char_occur.keys():
#    print(key, no_of_char_occur[key])

start = 0
max_length_substr = ''

for index in range(len(string)-1):
    if ( start >= index ):
        continue

    if (no_of_char_occur.get(string[index].lower()) < 2):
        start = index + 1
        continue

    substr = string[start:(index+1)].lower()
    substr_count = string.count(substr)
    if (  len(substr) >= len(max_length_substr) and substr_count > 1 ):
        max_length_substr = substr
    else:
        start = index

print('Max length substring is :', max_length_substr)
