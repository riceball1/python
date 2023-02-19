# defines how the values in an object can be iterated through


myList = [1, 2, 3]

# built in list iterator
for num in myList:
    print(num)


# more complex objects like binary search or linked list we can define our own

class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head) -> None:
        self.head = head
        self.cur = None

    # define iterator
    def __iter__(self):
        self.cur = self.head
        return self
    
    # iterate
    def __next__(self):
        # if not null
        if self.cur:
            val = self.cur.val
            self.cur = self.cur.next
            return val
        else:
            # if reached end then stop
            raise StopIteration
    
# test out the iteration
head = ListNode(1)
head.next = ListNode(2) # type: ignore
head.next.next = ListNode(3) # type: ignore
myList = LinkedList(head)




