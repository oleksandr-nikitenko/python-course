"""
Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own
workers. You should implement a method that allows you to add workers to a Boss. You're not allowed to add instances of
Boss class to workers list directly via access to attribute, use getters and setters instead!
"""


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.__workers = []
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__class__, self.name
    
    @property
    def workers(self):
        return self.__workers
    
    @workers.setter
    def workers(self, worker):
        self.__workers.append(worker)
    
    @workers.deleter
    def workers(self):
        self.__workers.clear()


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.__boss = boss
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'{self.__class__}: {self.name}'
    
    @property
    def boss(self):
        return self.__boss
    
    @boss.setter
    def boss(self, boss: Boss):
        if isinstance(boss, Boss):
            self.__boss = boss
        else:
            raise TypeError()
    
    @boss.deleter
    def boss(self):
        self.__boss = None
