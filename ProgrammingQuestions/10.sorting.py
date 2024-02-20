
# 1. Bubble Sort:
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Example usage:
array = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(array)
print("Bubble Sort Result:", array)


# 2. Selection Sort:
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Example usage:
array = [64, 34, 25, 12, 22, 11, 90]
selection_sort(array)
print("Selection Sort Result:", array)


# 3. Insertion Sort:
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Example usage:
array = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(array)
print("Insertion Sort Result:", array)


#  4. Merge Sort:
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Example usage:
array = [64, 34, 25, 12, 22, 11, 90]
merge_sort(array)
print("Merge Sort Result:", array)


# 5. Quick Sort:
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Example usage:
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = quick_sort(array)
print("Quick Sort Result:", sorted_array)


# 6. Heap Sort:
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# Example usage:
array = [64, 34, 25, 12, 22, 11, 90]
heap_sort(array)
print("Heap Sort Result:", array)


# 7. Counting Sort:
def counting_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    range_of_elements = max_value - min_value + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    for i in range(len(arr)):
        count[arr[i] - min_value] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    i = len(arr)- 1
    while i >= 0:
        output[count[arr[i] - min_value] - 1] = arr[i]
        count[arr[i] - min_value] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]


# Example usage:
array = [64, 34, 25, 12, 22, 11, 90]
counting_sort(array)
print("Counting Sort Result:", array)


# 8. Radix Sort:
def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10


# Example usage:
array = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(array)
print("Radix Sort Result:", array)


# 9. Shell Sort:
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


# Example usage:
array = [64, 34, 25, 12, 22, 11, 90]
shell_sort(array)
print("Shell Sort Result:", array)


# 10. Bucket Sort:
def bucket_sort(arr):
    buckets = []
    for i in range(len(arr)):
        buckets.append([])

    for num in arr:
        index = int(num * len(arr))
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    result = []
    for bucket in buckets:
        result += bucket

    return result


# Example usage:
array = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
sorted_array = bucket_sort(array)
print("Bucket Sort Result:", sorted_array)