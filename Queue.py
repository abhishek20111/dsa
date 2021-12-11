# import threading
# import time
# from collections import deque
#
#
# class Queue:
#     def __init__(self):
#         self.buffer = deque()
#
#     def enqueue(self,val):
#         self.buffer.append(val)
#
#     def dequene(self):
#         if len(self.buffer) ==0:
#             print("Quene is empty")
#             return
#         return self.buffer.pop()
#     def is_empty(self):
#         return len(self.buffer) == 0
#     def size(self):
#         return len(self.buffer)
#
#
# def place_order(orders):
#     for order in orders:
#         print("placing order for ",order)
#         food_order_queue.enqueue(order)
#         time.sleep(0.5)
#
# def service_order():
#     time.sleep(1)
#     while True:
#         order = food_order_queue.dequene()
#         print("now serving ...",order)
#         time.sleep(2)
# food_order_queue = Queue()
# if __name__ == '__main__':
#     orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
#     t1 = threading.Thread(target=place_order,args=(orders,))
#     t2 = threading.Thread(target=service_order)
#
#     t1.start()
#     t2.start()
#-----------------------------------------------Pratice--------------------------------------------------
# import threading
# from collections import deque
# import time
#
# class Queue:
#     def __init__(self):
#         self.buffer = deque()
#     def enumitrate(self,value):
#         self.buffer.append(value)
#     def deque(self):
#         if len(self.buffer) ==0:
#             print("empty ---")
#         return self.buffer.pop()
#     def empty(self):
#         return len(self.buffer)==0
#
# def place_order(orders):
#     for order in orders:
#         print("placing order--",order)
#         oder_from_queue.enumitrate(order)
#         time.sleep(0.5)
#
# def service_time():
#     time.sleep(1)
#     while True:
#         orders = oder_from_queue.deque()
#         print("now serving---",orders)
#         time.sleep(2)
#
#
# oder_from_queue = Queue()
# if __name__ == '__main__':
#     orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
#     t1 = threading.Thread(target = place_order,args = (orders,))
#     t2 = threading.Thread(target = service_time)
#
#     t1.start()
#     t2.start()

#-----------------------------------------------------------------------------------------------------------------
# from collections import  deque
#
# class Queue:
#     def __init__(self):
#         self.buffer = deque()
#
#     def enqueue(self, val):
#         self.buffer.appendleft(val)
#
#     def dequeue(self):
#         if len(self.buffer) == 0:
#             print("Queue is empty")
#             return
#
#         return self.buffer.pop()
#
#     def front(self):
#         return self.buffer[-1]
#
# def Product_binary_convert(n):
#     number_quene = Queue()
#     number_quene.enqueue("1")
#
#     for i in range(n):
#         front = number_quene.front()
#         print(" ",front)
#         number_quene.enqueue(front+"0")
#         number_quene.enqueue(front+"1")
#
#         number_quene.dequeue()
# if __name__ == '__main__':
#     Product_binary_convert(10)
#---------------------------------------------------pratice--------------------------------------------------------------
from collections import  deque

class Queue:
    def __init__(self):
        self.buffeer = deque()
    def enumirate(self,value):
        self.buffeer.appendleft(value)
    def deque(self):
        if len(self.buffeer)==0:
            print("queue is empty")
            return
        return self.buffeer.pop()
    def front(self):
        return self.buffeer[-1]

def Produce_to_binary(no):
    number_query = Queue()
    number_query.enumirate("1")
    for i in range(no):
        frontt = number_query.front()
        print(" ",frontt)
        number_query.enumirate(frontt+"0")
        number_query.enumirate(frontt+"1")

        number_query.deque()
if __name__ == '__main__':
    Produce_to_binary(10)