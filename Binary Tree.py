# class Binary_search_tree:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#     def add_child(self, data):
#         if data == self.data:
#             return
#
#         if data < self.data: #  if condition true than add element in left.
#             if self.left: #  check first left side is vaccant or not
#                 self.left.add_child(data) #  we will make new branch as position is filled
#             else:# as it is not filled so add data in vaccant point
#                 self.left = Binary_search_tree(data)
#
#         else:
#             if self.right:
#                 self.right.add_child(data)
#             else:
#                 self.right = Binary_search_tree(data)
#
#     def in_order_traversal(self): #  this method return list of element in binary tree specific order
#         element = []
#
#         #  visit left tree
#         if self.left:
#             element += self.left.in_order_traversal()
#
#         #  visit base node
#         element.append(self.data)
#
#         #  visit right node
#         if self.right:
#             element += self.right.in_order_traversal()
#
#         return element
#
#     def find_min(self):
#         if self.left is None:
#             return self.data
#         return self.left.find_min()
#
#     def find_max(self):
#         if self.right is None:
#             return self.data
#         return self.right.find_max()
#
#     def calculate_sum(self):
#         left_sum = self.left.calculate_sum() if self.left else 0
#         right_sum = self.right.calculate_sum() if self.right else 0
#         return self.data + left_sum + right_sum
#
#     def post_oder_traversal(self):
#         element = []
#         if self.left:
#             element += self.left.post_oder_traversal()
#         if self.right:
#             element += self.right.post_oder_traversal()
#
#         element.append(self.data)
#
#         return element
#
#     def pre_order_traversal(self):
#         element = [self.data]
#         if self.left:
#             element += self.left.pre_order_traversal()
#         if self.right:
#             element += self.right.pre_order_traversal()
#
#         return element
#
#     def search(self, val):
#         if self.data == val: #  it get the value at root node only
#             return True
#
#         if val < self.data: # might be possible in left side
#             if self.left: # if left side have element
#                 return self.left.search(val)
#             else: # if left side is empty
#                 return False
#
#         if val > self.data: #  might be possible in right side
#             if self.right:
#                 return self.right.search(val)
#             else:
#                 return False
#
# def build_tree(element): #  it just make easy to print
#     root = Binary_search_tree(element[0])
#
#     for i in range(1, len(element)):
#         root.add_child(element[i])
#
#     return root
#
#
# if __name__ == '__main__':
#
#     number = [43,3,4,23,4,3,4,344,3,43,343,4,32]
#     numbers_tree = build_tree(number)
#     print(numbers_tree.in_order_traversal())
#     #print(numbers_tree.search(4))
#
#     print("min ",numbers_tree.find_min())
#     print("max ",numbers_tree.find_max())
#     print("sum ",numbers_tree.calculate_sum())
#     print("In order traverse ",numbers_tree.in_order_traversal())
#     print("Post order traverse ",numbers_tree.post_oder_traversal())
#     #print("Post order traverse ",numbers_tree.post_oder_traversal())
#     #print("Pre order traverse ",numbers_tree.pre_order_traversal())
#     print("Pre order traverse ",numbers_tree.pre_order_traversal())
#----------------------------------------------Practice-------------------------------------------
# class Binary_Search_tree:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#     def add_child(self, data):
#         if data == self.data:
#             return
#         if data < self.data:
#             if self.left:
#                 self.left.add_child(data)
#             else:
#                 self.left = Binary_Search_tree(data)
#         else:
#             if self.right:
#                 self.right.add_child(data)
#             else:
#                 self.right = Binary_Search_tree(data)
#
#     def search(self, data):
#         if self.data == data:
#             return True
#
#         if data > self.data:
#             if self.right:
#                 return self.right.search(data)
#             else:
#                 return False
#         else:
#             if self.left:
#                 return self.left.search(data)
#             else:
#                 return False
#
#     def in_order_traversal(self):
#         element = []
#         if self.left:
#             element += self.left.in_order_traversal()
#
#         element.append(self.data)
#
#         if self.right:
#             element += self.right.in_order_traversal()
#
#         return element
#
#     def post_oder_traversal(self):
#         elements = []
#         if self.left:
#             elements += self.left.post_oder_traversal()
#         if self.right:
#             elements += self.right.post_oder_traversal()
#
#         elements.append(self.data)
#         return elements
#
#     def pre_oder_traversal(self):
#         elements = []
#         elements.append(self.data)
#
#         if self.right:
#             elements += self.right.pre_oder_traversal()
#         if self.left:
#             elements += self.left.pre_oder_traversal()
#         return elements
#
#     def find_max(self):
#         if self.right is None:
#             return self.data
#         # else: We not use else because it return all element in sequence of minimum and we need only one
#         return self.right.find_max()
#
#     def find_min(self):
#         if self.left is None:
#             return self.data
#         #else: We not use else because it return all element in sequence of minimum and we need only one
#         return self.left.find_min()
#
#     def calculate_sum(self):
#         left_sum = self.left.calculate_sum()if self.left else 0
#         right_sum = self.right.calculate_sum()if self.right else 0
#         return self.data + left_sum + right_sum
#
#     def delete(self, val):
#         if val < self.data:
#             if self.left:
#                 self.left = self.left.delete(val)
#
#         elif val > self.data:
#             if self.right:
#                 self.right = self.right.delete(val)
#         else:
#             if self.left is None and self.right is None:
#                 return None
#             elif self.left is None:  #  In cases were left is none it can be that there is right child which we need
#                 return self.right
#             elif self.right is None:
#                 return self.left
#
#             min_val = self.right.find_min()
#             self.data = min_val
#             self.data = self.right.delete(min_val)
#
#         return self
#
#
#
# def build_tree(element):
#     root = Binary_Search_tree(element[0])
#
#     for i in range(1, len(element)):
#         root.add_child(element[i])
#
#     return root
# if __name__ == '__main__':
#     number = [43,3,4,23,4,3,4,344,3,43,343,4,32]
#     number_tree = build_tree(number)
#
#     print("input number",number)
#     print("min ",number_tree.find_min())
#     print("max",number_tree.find_max())
#     print("sum ",number_tree.calculate_sum())
#     print("in traverse",number_tree.in_order_traversal())
#     print("post ",number_tree.post_oder_traversal())
#     print("pre ",number_tree.pre_oder_traversal())
#     print("delet ",number_tree.delete(3))
#     print(" number ",number_tree.in_order_traversal())

#------------------------------------------------Practice -2 -----------------------------

class Binerary_search_tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Binerary_search_tree(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.left.add_child(data)

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        element = []
        if self.left:
            element += self.left.in_order_traversal()
        element.append(self.data)

        if self.right:
            element += self.right.in_order_traversal()

        return element
    def post_order_traversal(self):
        elements =[]
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)
        return elements

