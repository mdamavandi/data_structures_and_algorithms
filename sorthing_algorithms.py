


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