


def selection_sort(numbers):
    """
    sorts the provided list in place
    :param numbers: list of numbers
    :return: None
    """
    for i in range(len(numbers)-1):

        # find index of smallest remaining element
        index_smallest = i
        for j in range(i+1, len(numbers)):

            if numbers[j] < numbers[index_smallest]:
                index_smallest = j

        # swap numbers[i] and numbers[index_smallest]
        numbers[i], numbers[index_smallest] = numbers[index_smallest], numbers[i]

def insertion_sort(numbers):
    """
    sorts the provided list in place
    :param numbers: list of numbers
    :return: None
    """
    for i in range(1, len(numbers)):
        j = i

        # insert numbers[i] into sorted part
        # stopping once numbers[i] in correct position
        while j > 0 and numbers[j] < numbers[j-1]:
            # swap numbers[j] and numbers[j-1]
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            j -= 1

def insertion_sort_interleaved(numbers, start_index, gap):
    """
    partially sorts the provided list in place, used in shell_sort()
    :param numbers: list to be sorted
    :param start_index: starting index
    :param gap: comparison distance
    :return: None
    """
    for i in range(start_index + gap, len(numbers), gap):
        j = i

        while (j - gap >= start_index) and (numbers[j] < numbers[j-gap]):
            numbers[j], numbers[j-gap] = numbers[j-gap], numbers[j]
            j -= gap

def shell_sort(numbers, gap_values):
    """
    sorts provided list in place
    :param numbers: list to sort
    :param gap_values: gaps to be sorted
    :return:
    """
    for gap_value in gap_values:
        for i in range(gap_value):
            insertion_sort_interleaved(numbers, i, gap_value)

def partition(numbers, start_index, end_index):
    """
    part of quicksort algorithm, works by partitioning section of unsorted list
    into left part and right part based on a pivot
    :param numbers: list to be sorted
    :param start_index:
    :param end_index:
    :return: last item in left part's index
    """
    # select the middle value as the pivot
    midpoint = start_index + (end_index - start_index) // 2
    pivot = numbers[midpoint]

    # 'low' and 'high' start at the ends of the list segment
    # and move towards each other
    low = start_index
    high = end_index

    done = False
    while not done:
        # increment low while numbers[low] < pivot
        while numbers[low] < pivot:
            low += 1

        # decrement high while pivot < numbers[high]
        while pivot < numbers[high]:
            high -= 1

        # if low and high have crossed each other, the loop is done
        # if not, the elements are swapped, low is incremented, and high is decremented
        if low >= high:
            done = True
        else:
            numbers[low], numbers[high] = numbers[high], numbers[low]
            low += 1
            high -= 1

    # 'high' is the last index in the left segment
    return high

def quicksort(numbers, start_index, end_index):
    """
    uses recursion to sort the two parts of the list
    :param numbers: list to be sorted
    :param start_index:
    :param end_index:
    :return: None
    """
    # only attempt to sort the list segment if there are at least two elements
    if end_index <= start_index:
        return

    # partition the list segment
    high = partition(numbers, start_index, end_index)

    # recursively sort the left segment
    quicksort(numbers, start_index, high)

    # recursively sort the right segment
    quicksort(numbers, high+1, end_index)

if __name__ == '__main__':
    numbers = [
        10,
        2,
        78,
        4,
        45,
        32,
        7,
        11,
    ]

    print(f'UNSORTED: {numbers}')

    selection_sort(numbers)

    print(f'SELECTION SORTED: {numbers}')

    numbers = [
        10,
        2,
        78,
        4,
        45,
        32,
        7,
        11,
    ]

    insertion_sort(numbers)

    print(f'INSERTION SORTED: {numbers}')

    numbers = [
        10,
        2,
        78,
        4,
        45,
        32,
        7,
        11,
    ]

    shell_sort(numbers, [4, 2, 1])

    print(f'SHELL SORTED: {numbers}')

    numbers = [
        12,
        18,
        3,
        7,
        32,
        14,
        91,
        16,
        8,
        57,
    ]

    print(f'UNSORTED: {numbers}')

    quicksort(numbers, 0, len(numbers)-1)
    print(f'QUICKSORTED: {numbers}')