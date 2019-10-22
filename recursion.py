

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

def gcd(n1, n2):
    """
    determines the greatest common divisor of two numbers,
    e.g. GCD(8, 12) = 4
    :param n1: first number
    :param n2: second number
    :return: greatest common divisor of n1 and n2
    """
    greatest_common_divisor = 0

    if n1 == n2: # base case, numbers are equal
        greatest_common_divisor = n1
    else: # recursive case, try again after subtracting the smaller number from the larger number
        if n1 > n2: # n2 is smaller
            greatest_common_divisor = gcd(n1 - n2, n2)
        else: # n1 is smaller
            greatest_common_divisor = gcd(n1, n2 - n1)

    return greatest_common_divisor

def scramble(r_letters, s_letters):
    """
    output every possible combination of a word
    each recursive call moves a letter from
    r_letters (remaining letters) to
    s_letters (scrambled letters)
    :param r_letters: remaining letters
    :param s_letters: scrambled letters
    :return:
    """
    if len(r_letters) == 0: # base case, all letters used
        print(s_letters)
    else: # recursive case
        # for each call to scramble() move a letter from remaining to scrambled
        for i in range(len(r_letters)):
            # the letter at index i will be scrambled
            scramble_letter = r_letters[i]

            # remove letter to scramble from remaining letters list

            remaining_letters = r_letters[:i] + r_letters[i+1:]

            # scramble letter
            scramble(remaining_letters, s_letters + scramble_letter)

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

    print('This program outputs the greatest\n'
          'common divisor of two numbers.\n')

    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))

    if (num1 < 1) or (num2 < 1):
        print('Note: neither value can be below 1')
    else:
        my_gcd = gcd(num1, num2)
        print(f'Greatest common divisor = {my_gcd}.')

    word = input('Enter a word to be scrambled: ')
    scramble(word, '')

