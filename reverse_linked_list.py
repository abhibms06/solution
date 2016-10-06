# reverse linked list without using additional DS

class Node:

    def __init__(self,data):
        self.next = None
        self.data = data

class solution:

    def insert(self,head,data):
        node = Node(data)
        if head == None:
            head = node
        else:
            cur = head
            while cur.next != None:
                cur = cur.next
            cur.next = node

        return head

    def showlist(self,head):
        cur = head
        while cur != None:
            print(cur.data,end=" ")
            cur = cur.next

    def reverselist(self,head):
        tmp1 = head
        cur = head.next
        head.next = None
        while cur != None:
            tmp2 = cur.next
            cur.next = tmp1
            head = tmp1 = cur
            cur = tmp2

        return head


s = solution()
head=None

for num in input().split():
    head = s.insert(head,int(num))

print("List items")
s.showlist(head)

print("\n\nReverse Linked list")
head = s.reverselist(head)
s.showlist(head)

