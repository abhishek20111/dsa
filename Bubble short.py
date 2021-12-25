# def bubble_sort(element):
#     size = len(element)
#
#     for i in range(size-1):
#         swapped = False
#         for j in range(size-1-i):# we have done this beacause it decrease some iteration as decrease time
#             if element[j] > element[j+1]:
#                 tmp = element[j]
#                 element[j] = element[j+1]
#                 element[j+1] = tmp
#                 swapped = True
#         if not swapped:# it is condition that if list is already a swap list not to do any other itertation and break it
#             break
#
# if __name__ == '__main__':
#     element = [5,6,7,3,53,32,56,34]
#
#     bubble_sort(element)
#     print(element)

#---------------------------------------------------------------------------------------------------------------------------------
def bubble_sort(element, key = None):
    size = len(element)

    for i in range(size - 1):
        swapped = True
        for j in range(size -1 -i):
            a = element[j][key]
            b = element[j+1][key]
            if a > b:
                tmp = element[j]
                element[j] = element[j+1]
                element[j+1] = tmp
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]

    bubble_sort(elements, key="transaction_amount")
    print(elements)