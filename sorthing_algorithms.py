


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

    print(f'SORTED: {numbers}')