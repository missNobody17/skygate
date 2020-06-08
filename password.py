from collections import Counter

def find_first_value(number):
    fill_digit = 0
    max_fill_digit_found = False
    new_number = []
    for digit in number:
        digit = int(digit)
        if digit >= fill_digit and not max_fill_digit_found:
            fill_digit = digit
        else:
            max_fill_digit_found = True

        new_number.append(fill_digit)

    return new_number

def find_all_passwords(cur_value, end_value):
    length = len(cur_value)
    # Two lists comparison.
    # The comparison uses lexicographical ordering:
    # first the first two items are compared, and if they differ
    # this determines the outcome of the comparison;
    # if they are equal, the next two items are compared, and so on,
    # until either sequence is exhausted.
    while cur_value < end_value:
        idx = length - 1
        for dgt in range(cur_value[idx], 10):
            cur_value[idx] = dgt
            yield cur_value

        while cur_value[idx] == 9 and idx > 0:
            idx -= 1

        fill_dgt = cur_value[idx] + 1
        for i in range(idx, length):
            cur_value[i] = fill_dgt

def compute(first_value, end_value):
    for val in find_all_passwords(first_value, end_value):
        # If all digits in the list are unique: the len(list) == len(set()).
        # Else at least one digit are repeated.
        if len(set(val)) < len(val):
            yield val


puzzle_input = "372002-809002"
start, end = puzzle_input.split('-')

first_value = find_first_value(start)
end = list(map(int, end))

print(sum(1 for _ in compute(first_value.copy(), end)))

# Answer is 475