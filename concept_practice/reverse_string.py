# Given an array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Example: Input: [0,1,0,3,12]; Output: [1,3,12,0,0]

# iteration one
# [0,1,0,3,12]

def return_zeros(array):
    ans_array = []

    for element in array:
        if element != 0:
            ans_array.append(element)

    number_of_zeros = len(array) - len(ans_array)

    for i in range(number_of_zeros):
        ans_array.append(0)

    return ans_array


print(return_zeros([0, 1, 0, 3, 12]))


def move_numbers(array):
    index_of_non_zero = 0

    for i in range(len(array)):
        if array[i] != 0:
            array[index_of_non_zero] = array[i]
            index_of_non_zero += 1

    for i in range(index_of_non_zero, len(array)):
        array[i] = 0

    return array.reverse()


print(move_numbers([0, 1, 0, 3, 12]))


def move_numbers_reverse(array):
    index_of_non_zero = len(array) - 1
    for i in range(len(array) - 1, -1, -1):
        if array[i] != 0:
            array[index_of_non_zero] = array[i]
            index_of_non_zero -= 1

    for i in range(index_of_non_zero + 1):
        array[i] = 0

    return array


print(move_numbers_reverse([0, 1, 0, 3, 12]))
