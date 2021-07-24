def isValidSubsequence(array, sequence):
    sequence_length = len(sequence)
    array_length = len(array)
    if sequence_length > array_length:
        return False

    count = 0
    for num_index, num_value in enumerate(array):
        if len(sequence) > 0 and sequence[0] == num_value:
            count += 1
            sequence.remove(sequence[0])

    if sequence_length == count:
        return True
    return False


if __name__ == '__main__':
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    # array = [1, 1, 6, 1]
    # sequence = [1, 1, 1, 6]
    sequence = [22, 25, 6]
    # sequence = [1, 6, -1, 10]
    print(isValidSubsequence(array, sequence))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
