


def linear_search(numbers, key):
    """
    find the location of some key in a list or indicate the key is not in the list
    :param numbers: list to be searched
    :param key: item to be found
    :return: index of key in numbers or -1 if not found
    """
    for i in range(len(numbers)):
        if (numbers[i] == key):
            return i
    # key was not found in numbers
    return -1

def binary_search(numbers, key):
    """
    find the location of some key in a list or indicate the key is not in the list
    :param numbers: list to be searched
    :param key: item to be found
    :return: index of key in numbers or -1 if not found
    """
    # variables to hold the low, middle, and high indices of the areas being searched
    # starts with entire range
    low = 0
    mid = len(numbers) // 2
    high = len(numbers) - 1

    # loop until 'low' passes 'high'
    while (high >= low):
        # calculate the middle index
        mid = (high + low) // 2

        # cut the range to either the left or right half
        # unless numbers[mid] is the key
        if (numbers[mid] < key):
            low = mid + 1

        elif (numbers[mid] > key):
            high = mid - 1

        else:
            return mid
    # not found
    return -1

if __name__ == '__main__':
    numbers = [
        2,
        4,
        7,
        10,
        11,
        32,
        45,
        87,
    ]
    print(f'NUMBERS: {numbers}')

    key = int(input('Linear search; enter an integer value: '))
    key_index = linear_search(numbers, key)

    if (key_index == -1):
        print(f'{key} was not found.')
    else:
        print(f'Found {key} at index {key_index}.')

    key = int(input('Binary search; enter an integer value: '))
    key_index = binary_search(numbers, key)

    if (key_index == -1):
        print(f'{key} was not found.')
    else:
        print(f'Found {key} at index {key_index}.')