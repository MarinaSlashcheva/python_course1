class fibonacci_sequence:
    def __init__(self, length):
        self.length = length
        self.count = 0
        self.start = 1
        self.add = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.length:
            output = self.start + self.add
            self.start = self.add
            self.add = output
            self.count += 1
            return output
        else:
            raise StopIteration

seq = fibonacci_sequence(11)
for i in seq:
    print(i)