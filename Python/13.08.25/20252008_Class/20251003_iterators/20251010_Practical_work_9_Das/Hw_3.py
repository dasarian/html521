def filter_and_square(numbers, threshold):
    for num in numbers:
        if num > threshold:
            yield num ** 2

if __name__ == "__main__":
    nums_str = input("Введите числа через пробел: ")
    numbers = [int(x) for x in nums_str.split()]
    threshold = int(input("Введите пороговое значение: "))

    for result in filter_and_square(numbers, threshold):
        print(result)