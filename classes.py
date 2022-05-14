class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"hello, my name is {self.name}"

    def say_age(self):
        return f"hello, my name is {self.age}"


person_one = Person("Ivan", 28)
person_two = Person("Egor", 999)


class Boy(Person):
    def __init__(self, name, age, music):
        super().__init__(name, age)
        self.music = music

    def say_hello(self):
        return f"hello, dear, my name is {self.name}"

    def say_hello_and_music(self):
        return f"hello, my name is {self.name}, i'm listening to {self.music}"


boy_one = Boy("Lex", 13, "Bah")

print(boy_one.say_hello_and_music())
print(boy_one.say_hello())
