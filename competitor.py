class Competitor:
    # used to initialise variables that all functions can access
    def __init__(self):
        self.array = []
        self.N = 0
        self.i_max = -1  # index of the maximum element
        # feel free to add your own variables to track anything else

    def push(self, key):
        self.array.append(key)
        if self.i_max == -1 or key > self.array[self.i_max]:
            self.i_max = self.N
        self.N += 1


    def pop(self):
        if self.i_max == -1:
            return None

        key_max = self.array[self.i_max]

        # Move last item into max position
        self.N -= 1
        self.array[self.i_max] = self.array[self.N]

        # Remove last item
        self.array.pop()

        # Empty now
        if self.N == 0:
            self.i_max = -1
            return key_max

        # Find new maximum
        self.i_max = 0

        for i in range(1, self.N):
            if self.array[i] > self.array[self.i_max]:
                self.i_max = i

        return key_max
    

    def getTop(self):
        if self.i_max == -1:
         return None

        return self.array[self.i_max] 