


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

def merge(numbers, i, j, k):
    """
    divides list into two halves, recursively sorts each half,
    then merges sorted halves to produce a sorted list
    :param numbers: list of numbers containing 2 sorted partitions to merge
    :param i: start index of first sorted partition
    :param j: end index of first sorted partition
    :param k: end index of second sorted partition
    :return:
    """
    merged_size = k - i + 1 # size of merged partition
    merged_numbers = [0] * merged_size # dynamically allocates temporary array for merged numbers

    merge_pos = 0 # position to insert merged number
    left_pos = i # initialize left partition position
    right_pos = j + 1 # initialize right partition position

    # ad smallest element from left or right partition to merged numbers
    while left_pos <= j and right_pos <= k:
        if numbers[left_pos] <= numbers[right_pos]:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos += 1
        else:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos += 1
        merge_pos = merge_pos + 1

        # if left partition is not empty, add remaining elements to merged numbers
        while left_pos <= j:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos += 1
            merge_pos += 1

        # if right partition is not empty, add remaining elements to merged numbers
        while right_pos <= k:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos += 1
            merge_pos += 1

        # copy merge number back to numbers
        for merge_pos in range(merged_size):
            numbers[i+merge_pos] = merged_numbers[merge_pos]


def merge_sort(numbers, i, k):
    """
    recursively sorts a partition of a greater list
    :param numbers: list with partition to sort
    :param i: start index of partition to sort
    :param k: end index of partition to sort
    :return:
    """
    j = 0

    if i < k:
        j = (i + k) // 2 # find the midpoint in the partition

        # recursively sort left and right partitions
        merge_sort(numbers, i, j)
        merge_sort(numbers, j+1, k)

        # merge left and right partition in sorted order
        merge(numbers, i, j, k)

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

    numbers = [
        61,
        76,
        19,
        4,
        94,
        32,
        27,
        83,
        58,
    ]

    print(f'UNSORTED: {numbers}')

    merge_sort(numbers, 0, len(numbers)-1)
    print(f'MERGE SORTED: {numbers}')