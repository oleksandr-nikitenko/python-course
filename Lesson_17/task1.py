"""
Create your own implementation of a built-in function enumerate, named `with_index`, which takes two parameters:
`iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function
"""


class with_index:
    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.start = start
        self.i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i == len(self.iterable):
            raise StopIteration
        result = self.start, self.iterable[self.i]
        self.i += 1
        self.start += 1
        return result


for i in with_index(['a', 'b', 'c', 'd'], 1):
    print(i)
