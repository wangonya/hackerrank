# https://www.hackerrank.com/challenges/30-linked-list/problem


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # The function gets called with the whole linked list.
        # If the list is empty, insert the element as the head.
        # Otherwise if there is no element after the head,
        # put the data after the head.
        # Otherwise,
        # call the function with all of the elements except for the current head
        if not head:
            head = Node(data)
        elif not head.next:
            head.next = Node(data)
        else:
            self.insert(head.next, data)
        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
