def twoNumberSum(array, targetSum):
    # Write your code here.
    result_array = []
    for i, value_at_i in enumerate(array):
        print(f'i-index-> {i}: {value_at_i}')
        remaining_arr = array[i+1:]
        for j, value_at_j in enumerate(remaining_arr):
            if(addToGetTargetSum(value_at_i, value_at_j, targetSum)):
                return [value_at_i, value_at_j]
    return result_array

def addToGetTargetSum(num1, num2, targetSum):
    return num1 + num2 == targetSum


if __name__ == '__main__':
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10
    print(twoNumberSum(array, targetSum))
