def guardian(func):
    def inner(*args, **kwargs):
        neighbors = ["Иван", "Алекей"]
        if args[0] in neighbors:
            func(*args, **kwargs)
        else:
            print("тебе сюда нельзя, гав-гав")
    return inner


@guardian
def say_hello(visitor):
    print(f"Привет, {visitor}")


if __name__ == '__main__':
    visitors = ["коля", "Иван", "Николай", "Глеб"]
    for visitor in visitors:
        say_hello(visitor)

