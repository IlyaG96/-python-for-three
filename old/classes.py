class User:
    def __init__(self, name, age, work):
        self.name = name
        self.age = age
        self.work = work

    def say_hello(self):
        return f"hello, my name is {self.name}"


user1 = User('Egor', '28', 'python')


class Child(User):
    def __init__(self, name, age, work, music):
        super().__init__(name, age, work)
        self.music = music

    def say_music(self):
        return f"hello, my name is {self.name}, i'm listening to {self.music}"


child1 = Child('Ivan', '13', 'python', 'Bah')
