# def insertion_sort(elements):
#     for i in range(1, len(elements)):
#         pointer = elements[i]
#         j = i - 1
#         while j >= 0 and pointer < elements[i]:
#             elements[j+1] = elements[j]
#             j = j+1
#         elements[j+1] = pointer

def insertion_sort(my_list):
    for index in range(1, len(my_list)):
        current_value = my_list[index]
        position = index
        while current_value < my_list[position - 1] and position >= 0:# it just condition that is element of left side is greater or not
            my_list[position] = my_list[position - 1] # it give value of element from last element
            position -= 1# just to decrement postion
        my_list[position] = current_value # if while loop condition is false as left element is not smaller so we do not sift element we put that as it is


if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    insertion_sort(elements)
    print(elements)
    #
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        insertion_sort(elements)
        print(f'sorted array: {elements}')