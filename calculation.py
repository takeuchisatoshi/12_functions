def calculation_sum(numbers):
    total = 0

    for num in numbers:
        total += num
    return total


if __name__ == '__main__':
    numbers = [34, 12, 59, 4]
    total = calculation_sum(numbers)
    print(total)
