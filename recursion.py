

def binary_search(low, high):
    """
    guessing game using binary search, range is built using low/high
    :param low: low number
    :param high: high number
    :return:
    """
    mid = (high + low) // 2 # midpoint of low to high
    answer = input(f'Is it {mid}? (l/h/y): ')

    if (answer != 'l') and (answer != 'h'): # base case
        print('Got it!')
    else:
        if answer == 'l':
            binary_search(low, mid)
        else:
            binary_search(mid+1, high)

def list_binary_search(lst, item, low, high):
    """
    finds index of string in list of strings, else -1
    searches only the index range low to high
    note: upper/lower case characters matter
    :param lst: list to be searched, sorted
    :param item: item to be found
    :param low: lowest index
    :param high: highest index
    :return:
    """
    range_size = (high - low) + 1
    mid = (high + low) // 2

    if item == lst[mid]: # base case 1, found at mid
        pos = mid
    elif range_size == 1: # base case 2, not found
        pos = -1
    else: # recursive search, search lower or upper half
        if item < lst[mid]: # search lower half
            pos = list_binary_search(lst, item, low, mid)
        else: # search upper half
            pos = list_binary_search(lst, item, mid+1, high)

    return pos

def fibonacci(v1, v2, run_cnt):
    """
    output the Fibonacci sequence step-by-step
    Fibonacci sequence starts as:
    0 1 1 2 3 5 8 13 21 ... in which the first
    two numbers are 0 and 1 and each additional
    number is the sum of the previous two numbers
    :param v1: element in Fibonacci sequence
    :param v2: next element in Fibonacci sequence
    :param run_cnt: number of steps to take
    :return:
    """
    print(f'{v1} + {v2} = {v1+v2}')

    if run_cnt <= 1: # base case, ran for user's number of steps
        pass # do nothing
    else: # recursive case
        fibonacci(v2, v2+v1, run_cnt-1)

if __name__ == '__main__':
    print('Choose a number from 0 to 100.')
    print('Answer with:')
    print('    l (your num is lower)')
    print('    h (your num is higher)')
    print('  any other key (guess is right).')

    binary_search(0, 100)

    attendees = []

    attendees.append('Adams, Mary')
    attendees.append('Carver, Michael')
    attendees.append('Domer, Hugo')
    attendees.append('Fredericks, Carlo')
    attendees.append('Li, Jie')

    name = input('Enter person\'s name: Last, First: ')
    pos = list_binary_search(attendees, name, 0, len(attendees)-1)

    if pos >= 0:
        print(f'Found at position {pos}.')
    else:
        print('Not found.')

    print('This program outputs the \n'
          'Fibonacci sequence step-by-step,\n'
          'starting after the first 0 and 1.\n')

    run_for = int(input('How many steps would you like? '))

    fibonacci(0, 1, run_for)