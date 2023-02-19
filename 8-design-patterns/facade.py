# outward appearance hides more complex details
# e.g. http client or dynamic arrays

# facade

# python arrays are dynamic by default, but this is an example of resizing

class Array:
    def __init__(self) -> None:
        self.capacity = 2
        self.length = 0
        self.arr = [0] * 2 # array of capacity  = 2

    # insert n in the last position of the array
    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()

        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1

    def resize(self):
        # create new array of double capacity
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        # copy elements to newArr
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr

    # remove the last element in the array
    def popback(self):
        if self.length > 0:
            self.length -= 1