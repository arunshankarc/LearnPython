class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    # Now we need iter() to run to return iterator over iterable
    def __iter__(self):
        return self

    # Now when iterator is created, something should invoke next
    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current = self.current + 1
            return num
        raise StopIteration


for x in Counter(0, 10):
    print(x)
