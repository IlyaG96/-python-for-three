def guardian(func):
    def inner(*args, **kwargs):
        allowed_peoples = ["Иван", "Алексей", "Марина"]
        if args[0] in allowed_peoples:
            func(*args, **kwargs)
        else:
            print(f"Тебе сюда нельзя! {args[0]}")

    return inner


@guardian
def say_hello(visitor, guest="Рома"):
    print(f"hello! {visitor}")


if __name__ == '__main__':
    visitors = ["Иван", "Алексей", "Марина", "Николай", "Геннадий"]
    for visitor in visitors:
        say_hello(visitor)