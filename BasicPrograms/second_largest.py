def sort(numbers):
    for i in range(0, len(numbers)):
        for j in range(0, i):
            if numbers[i] < numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp


numbers = [1, 4, 7, 8, 5, 2, 0, 3, 6, 9]
print(numbers)
sort(numbers)
print(numbers)
