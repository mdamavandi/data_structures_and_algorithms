


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

    key = int(input('Enter an integer value: '))
    key_index = linear_search(numbers, key)

    if (key_index == -1):
        print(f'{key} was not found.')
    else:
        print(f'Found {key} at index {key_index}.')