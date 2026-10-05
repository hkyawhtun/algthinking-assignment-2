class MaxHeap:
    # used to initialise variables that all functions can access
    def __init__(self):
        self.array = [None]  # index 0 is unused
        self.N = 0
        # feel free to add your own variables to track anything else

    def bubbleUp(self, i):
     while i > 1:
        parent = i // 2

        if self.array[i] <= self.array[parent]:
            break

        self.array[i], self.array[parent] = \
            self.array[parent], self.array[i]

        i = parent


    def bubbleDown(self, i):
        while True:
            left = 2 * i
            right = 2 * i + 1
            largest = i

            if left <= self.N and self.array[left] > self.array[largest]:
                largest = left

            if right <= self.N and self.array[right] > self.array[largest]:
                largest = right

            if largest == i:
                break

            self.array[i], self.array[largest] = \
                self.array[largest], self.array[i]

            i = largest

            
    def push(self, key):
            self.array.append(key)
            self.N += 1
            self.bubbleUp(self.N)

    def pop(self):
        # Empty heap
        if self.N == 0:
            return None

        # Save maximum value
        key_max = self.array[1]

        # If only one element
        if self.N == 1:
            self.array.pop()
            self.N = 0
            return key_max

        # Move last element to root
        self.array[1] = self.array[self.N]

        # Remove old last element
        self.array.pop()

        self.N -= 1

        # Restore max-heap property
        self.bubbleDown(1)

        return key_max

    def getTop(self):
        if self.N == 0:
            return None
        return self.array[1]

    def heapify(self, H, n):
        # H is a normal Python list of keys
        self.array = [None] + H[:n]
        self.N = n

        # Leaves are already valid heaps.
        # Start at last parent and work upward.
        for i in range(self.N // 2, 0, -1):
            self.bubbleDown(i)