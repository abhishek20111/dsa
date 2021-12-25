# def linear_search(number_list, number_to_find):
#     for index, element in enumerate(number_list):
#         if element == number_to_find:
#             return index
#         return -1
#
#
# def binary_search(number_list, number_to_find):
#     left_index = 0
#     right_index = len(number_list) - 1 # as index start from 0
#     mid_number = 0
#     while left_index <= right_index:
#         mid_index = (left_index + right_index)//2 # to get integer in output not float
#         mid_number = number_list[mid_index]
#
#         if mid_number == number_to_find:
#             return mid_index
#         if mid_number < number_to_find:
#             left_index = mid_index + 1
#         else:
#             right_index = mid_index - 1
#
#     return -1
#
# def binary_search_recursion(number_list, number_to_find, left_index, right_index): # it just search any no in particular boundary of index
#     if right_index < left_index: # right side is always greater than left
#         return -1
#
#     mid_index = (left_index + right_index)//2
#     mid_number = number_list[mid_index]
#
#     if mid_index >= len(number_list) or mid_index <0:
#         return -1
#
#     if mid_number == number_to_find:
#         return mid_index
#
#     if mid_number < number_to_find:
#         left_index = mid_index + 1
#     else:
#         right_index = mid_index - 1
#
#     return binary_search_recursion(number_list, number_to_find, left_index, right_index)
#
# if __name__ == '__main__':
#     number_list = [12, 15, 17, 19, 25, 45, 67]
#     numbers = [1, 4, 6, 9, 10, 5, 7]
#     number_to_find = 45
#     number_to_find1 = 17
#
#     # number_list = [i for i in range(1000001)]  # just for checking time taken by linear search
#     # index = linear_search(number_list, number_to_find1)
#
#     index = linear_search(number_list, number_to_find)
#     print(f"No. foound at {index} using linear search")
#     index = binary_search(number_list, number_to_find1)
#     print(f"No. found at {index} using binary search")
#     index = binary_search_recursion(number_list, number_to_find,0, len(number_list))
#     print(f"No. found at {index} using binarary search recursion")
#     index = binary_search_recursion(numbers, number_to_find,0, len(numbers))
#     print(f"No. found at {index} using binarary search recursion in number")

#-----------------------------------------------------------------Pratice-----------------
def binary_search(number_list, number_to_find):
    left_index = 0
    right_index = len(number_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index)//2
        mid_number = number_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index +1
        else:
            right_index = mid_index -1
    return -1
def find_all_occurance(number, number_to_find):
    index = binary_search(number, number_to_find)
    indices = [index]
    # find indices in left hand side
    i = index - 1
    while i >=0:
        if number[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i -1

    i = index +1
    while i< len(number):
        if number[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i +1
    return sorted(indices)

if __name__ == '__main__':
    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 15
    indices = find_all_occurance(numbers, number_to_find)
    print(f"Indices of occurances of {number_to_find} are {indices}")
    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 1
    indices = find_all_occurance(numbers, number_to_find)
    print(f"Indices of occurances of {number_to_find} are {indices}")

