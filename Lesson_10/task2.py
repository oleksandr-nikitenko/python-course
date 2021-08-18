"""Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age.
Then create a method `human_age` which returns the dog’s age in human equivalent."""


class DogWith:
    """Doggy age"""
    age_factor = 7
    
    def __init__(self, dogs_age: int) -> None:
        self.dog_age = dogs_age
    
    def human_age(self) -> int:
        return self.age_factor * self.dog_age
    
    
obj = DogWith(8)
print(obj.human_age())
