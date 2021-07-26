def sortedSquaredArray(array):
    squared_array = []
    for num in array:
        squared_array.append(num*num)
    return sorted(squared_array)

if __name__ == '__main__':
    # array = [1, 2, 3, 5, 6, 8, 9]
    array = [-2, 1]
    print(array)
    print(sortedSquaredArray(array))
