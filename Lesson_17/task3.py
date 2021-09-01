"""
Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for
retrieving elements using square brackets syntax.
"""


class MyIterableSquare:
    
    def __init__(self, ls: list):
        self.__ls = MyIterableSquare.__squares(ls)
        self.__current = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__current < len(self.__ls) - 1:
            self.__current += 1
            return self.__ls[self.__current - 1]
        else:
            raise StopIteration
    
    @staticmethod
    def __squares(ls):
        result = []
        for val in ls:
            result.append(val**2)
        return result
            
    def __getitem__(self, item=0):
        return self.__ls[item]
    
    
obj = MyIterableSquare([1, 2, 3, 4, 5])

print(obj[0:3])

for i in obj:
    print(i)