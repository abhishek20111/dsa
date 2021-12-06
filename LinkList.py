# class Node:
#     def __init__(self,data = None,next = None): # get data of other
#         self.data = data #data of given value
#         self.next = next  # next elemt
#
# class Linklist:
#     def __init__(self):
#         self.head = None #head mean 1'st element
#
#     def insert_at_begining(self,data):
#         node = Node(data, self.head) # it mean at first add data and then header(mean first element)
#         self.head = node #as new head is now node
#
#     def print(self):
#         if self.head is None:
#             print("linklist is empty ")
#             return
#         itr = self.head #now we see element one by one starting from head
#         llstr ='' # make empty string to add value
#
#         while itr:
#             llstr += str(itr.data) + '--->' #append data
#             itr = itr.next #go to next element
#
#         print(llstr)
#
#     def insert_at_end(self,data):
#         if self.head is None: #head mean first element is empty
#             self.head = Node(data,None) #now it take head to node with (data,next) take data and move next element
#             return
#         itr = self.head # to iterate element one by one
#         while itr.next:
#             itr = itr.next #(it take till ite.next became null)
#
#         itr.next = Node(data,None) #( so when we get last position)
#
#     def insert_values(self,data_list):  # ( In this make a function to add element in list)
#         self.head = None # let the starting to iterate
#         for data in data_list:
#             self.insert_at_end(data)
#
#     def get_length(self):  #it will just give length of element
#         count = 0
#         itr = self.head
#         while itr:
#             count +=1
#             itr = itr.next
#
#         return count
#
#     def remove_at(self,index):  #it remove element
#         if index<0 or index >= self.get_length():
#             raise Exception("Invalid index")
#
#         if index == 0: #remove element in beinging of list
#             self.head = self.head.next #in head it put second element
#             return
#
#         count =0
#         itr = self.head # initilise itr to start from 0
#         while itr:# start counting itr
#             if count == index-1:# we stop search one step before
#                 itr.next = itr.next.next# move next element
#                 break
#
#             itr = itr.next
#             count +=1
#
#     def insert_at(self,index,data):
#         if index < 0 or index > self.get_length():
#             raise Exception("Invalid index")
#
#         if index == 0:
#             self.insert_at_begining(data)
#             return
#         count =0
#         itr = self.head
#         while itr:
#             if count == index -1: # (beacuse when we inserting element we have to modify the next pointer of previous element)
#                 node = Node(data,itr.next)#make a node and call Node class beacuse we are in previous element ,so it take data and put on next element
#                 itr.next = node
#                 break
#
#             itr = itr.next
#             count +=1
#
#
# if __name__ == '__main__':
#     ll = Linklist()
#     ll.insert_values(["bana","man","grap","orag","kuku"])
#     ll.insert_at_begining(5)
#     # ll.insert_at_begining(56)
#     # ll.insert_at_begining(543)
#     ll.insert_at_end(45)
#     ll.remove_at(2)
#     ll.insert_at(3,"dfsfd")
#     ll.print()
#     print("length",ll.get_length())






#---------------------------------------------Practice by adding some extre----------------------------------------------
#
# class Node:
#     def __init__(self,data = None,next = None):
#         self.data = data
#         self.next = next
#
# class Listlisting:
#     def __init__(self):
#         self.head = None
#
#     def inserting_at_beging(self,data):
#         node = Node(data,self.head)
#         self.head = node
#
#     def print(self):
#         if self.head is None:
#             print("Empty list")
#             return
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data) + '--->'
#             itr = itr.next
#         print(llstr)
#
#     def inserting_at_end(self,data):
#         if self.head is None:
#             self.head = Node(data,None)
#             return
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#
#         itr.next = Node(data,None)
#
#     def insert_value(self, data_list):
#         #self.head = None
#         for data in data_list:
#             self.inserting_at_end(data)
#
#
#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count +=1
#             itr = itr.next
#
#         return count
#
#     def remove_at(self,index):
#         if index < 0 or index > self.get_length():
#             raise Exception("Invalid Index")
#         if index == 0:
#             self.head = self.head.next
#             return
#         itr = self.head
#         count =0
#         while itr:
#             count = index -1
#             itr.next = itr.next.next
#             break
#
#         itr = itr.next
#         count += 1
#     def insert_at(self,index,data):
#         if index <0 or index >self.get_length():
#             print("enter in range")
#             return
#         if index == 0:
#             self.inserting_at_beging(data)
#
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index -1:
#                 nobe = Node(data,itr.next)
#                 itr.next = nobe
#                 break
#
#             itr = itr.next
#             count += 1
#
#     def insert_after_value(self,data_after,data_to_insert):
#         if data_after is None:
#             print("Invalid value")
#             return
#
#         if self.head.data == data_after:
#             self.head.next = Node(data_to_insert,self.head.next)
#             return
#
#         itr = self.head
#         while itr:
#             if itr.data == data_after:
#                 itr.next = Node(data_to_insert,itr.next)
#                 break
#
#             itr = itr.next
#
#     def remove_by_value(self, data):
#         if data is None:
#             return
#         if self.head.data == data:
#             self.head = self.head.next
#
#         itr = self.head
#         while itr.next:
#             if itr.next.data == data:
#                 itr.next = itr.next.next
#                 break
#             itr = itr.next
#
#
# if __name__ == '__main__':
#     li = Listlisting()
#     li.inserting_at_beging(45)
#     li.inserting_at_beging(87)
#     li.inserting_at_beging(445)
#     li.insert_value(["fr","kj","lk","kg"])
#     li.print()
#     li.remove_at(2)
#     li.print()
#     print(li.get_length())
#     li.insert_at(2,"hhhhhhh")
#     li.insert_after_value("fr","gg")
#     li.print()
#     li.remove_by_value("kg")
#     li.print()




#---------------------------------------------Practice by adding some extra in Node (DOUBLY LINK LIST)----------------------------------------------

class Node:
    def __init__(self,data = None,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Listlisting:
    def __init__(self):
        self.head = None

    def inserting_at_beging(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Empty list")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '<--->'
            itr = itr.next
        print(llstr)

    def forward_direction(self):
        if self.head is None:
            raise Exception("nothing is in list")

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)

    def print_rev(self):
        if self.head is None:
            raise Exception("nothing is in list")

        itr = self.head
        llstr1 = ''
        while itr:
            llstr1 += str(itr.data) + '<---'
            itr = itr.prev
        print("Link list in reverse :", llstr1)


if __name__ == '__main__':
    li = Listlisting()
    li.inserting_at_beging("67")
    li.inserting_at_beging("0866hg")
    li.inserting_at_beging("hjf")
    li.inserting_at_beging("6787")
    li.print()
    li.forward_direction()
    li.print_rev()
