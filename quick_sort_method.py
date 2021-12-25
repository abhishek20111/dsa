# def swap(a, b, arr):
#     if a!=b:
#         tmp = arr[a]
#         arr[a] = arr[b]
#         arr[b] = tmp
#
# def partition(elements, start, end): #by putting start and end we give the place of pivot also
#     # pivot_index = start
#     # pivot = elements[pivot_index]
#     pivot_index = start
#     pivot = elements[pivot_index]
#
#     # start = pivot_index + 1 #just intilizing position
#     # end = len(elements) - 1 #just intilizing position
#
#     while start < end: #it is very important to stop loop when start and end are at same point and they are going to cross each
#         while start < len(elements) and elements[start] <= pivot:#it is the no greater than pivot
#             start += 1
#
#
#         while elements[end] > pivot:# it is for no less than pivot
#             end -= 1
#
#         if start < end:# it just swap element continuosly as recuried
#             swap(start, end, elements)
#
#     swap(pivot_index, end, elements)# it do last step of HAORE PARTITON to swap that element with pivot
#
#     return end
#
# def quick_sort(elements, start, end):
#     if start < end: #it help to stop
#         #pi = partition(elements, start, end)
#         pi = partition(elements, start, end)
#         quick_sort(elements, start, pi-1) #  this is recursive approach that call it to partition index -1(left partition)
#         quick_sort(elements, pi+1, end)   #  this is recursive approach that call it to partition index +1(right partition)
# #
# if __name__ == '__main__':
#     elements = [11, 9, 29, 7, 2, 15, 28]
#     quick_sort(elements, 0, len(elements)-1)
#     print(elements)
#     tests = [
#         [11, 9, 29, 7, 2, 15, 28],
#         [3, 7, 9, 11],
#         [25, 22, 21, 10],
#         [29, 15, 28],
#         [],
#         [6]
#     ]
#     for elements in tests:
#         quick_sort(elements, 0, len(elements)-1)
#         print(f'sorted array: {elements}')
#------------------------------------------------------------Pratice(some additional with new type)------------------------------
#----------------------------------------------------------- lumoto partition scheme----------------------------

# def swap(a, b, arr):
#     if a != b:
#         tmp = arr[a]
#         arr[a] = arr[b]
#         arr[b] = tmp
#
# def quick_sort(element, start, end):
#     if len(element) == 1:
#         return
#     if start < end:
#         pi = partition(element, start, end)
#         quick_sort(element, start, pi-1)
#         quick_sort(element, pi+1, pi-1)
#
# def partition(element, start, end):
#     pivot = element[end]
#     p_index = start
#
#     for i in range(start, end):
#         if element[i] <= pivot:
#             swap(i, p_index, element)
#             p_index += 1
#
#     swap(p_index, end, element)
#     return p_index
#
# if __name__ == '__main__':
#     tests = [
#         [11, 9, 29, 7, 2, 15, 28],
#         [3, 7, 9, 11],
#         [25, 22, 21, 10],
#         [29, 15, 28],
#         [],
#         [6]
#     ]
#
#     for element in tests:
#         quick_sort(element, 0, len(element)-1)
#         print(f'sorted array,{element}')