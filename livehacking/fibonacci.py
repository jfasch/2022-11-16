def fibonacci():
    first, second = 1, 1

    yield first
    yield second

    while True:
        next = first + second
        yield next
        first, second = second, next

if __name__ == '__main__':
    fibo_numbers = fibonacci()

    for number in fibo_numbers:
        print(number)
