from operator import itemgetter
import operator

class Book():

    def __init__(self,name,height,width,edge,weight):
        self.name = name
        self.height = height
        self.width = width
        self.edge = edge
        self.weight = weight

b1 = Book('mybook1',45,21,4,5)
b3 = Book('mybook3',34,45,2,78)
b2 = Book('mybook2',45,2,4,35)


objects = [b1, b2, b3]

# Display current books
print('###Display current books###')
print('Name','Height','Width','Edge','Weight', sep='\t')
for i in range(len(objects)):
    obj = objects[i]
    print(obj.name,obj.height,obj.width,obj.edge,obj.weight, sep='\t')

# Insert into books array
books = []
for obj in objects:
    books.append([obj.name, obj.height, obj.width, obj.edge, obj.weight])

# Sort based on input by user
print()
print('##Enter input to sort the books##')
print('Ex : 3 2 would sort based on Book width and height')
print('1. Sort based on book name')
print('2. Sort based on book height')
print('3. Sort based on book width')
print('4. Sort based on book edge')
print('5. Sort based on book weight')
print('Enter your input : ',sep=' ')

order = [ int(tmp) for tmp in input().split() ]

#Decrease all index value by 1 since we are storing in array
order = list(map(lambda num:num-1, order))

# validation can be added to make sure user input is 0 <= 5
if (len(order) == 1):
    books.sort(key=operator.itemgetter(order[0]))
elif(len(order) == 2):
    books.sort(key=operator.itemgetter(order[0],order[1]))
elif(len(order) == 3):
    books.sort(key=operator.itemgetter(order[0],order[1],order[2]))
elif(len(order) == 4):
    books.sort(key=operator.itemgetter(order[0],order[1],order[2],order[3]))
else:
    books.sort(key=operator.itemgetter(order[0],order[1],order[2],order[3], order[4]))

print('\n###Display sorted books###')
print('Name','Height','Width','Edge','Weight', sep='\t')
for i in range(len(books)):
    print(str(books[i]).strip('[]'))

