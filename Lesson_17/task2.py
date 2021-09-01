"""
Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
`start`, `end`, and optional step. Tips: See the documentation for `range` function
"""


class in_range:
    
    def __init__(self, start: int, end: int, step: int = 1):
        self.__result = int()
        if isinstance(start, int) and isinstance(end, int) and isinstance(step, int):
            self.start = start
            self.end = end
            self.step = step
        else:
            raise TypeError
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start > self.end - 1:
            raise StopIteration
        self.__result = self.start
        self.start += self.step
        return self.__result


for i in in_range(1, 6):
    print(i)
    