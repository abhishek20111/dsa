# class Harsh_Table:
#     def __init__(self):
#         self.Max = 100
#         self.arr = [[] for i in range(self.Max)]
#
#     def get_harsh(self,key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.Max
#
#     def __getitem__(self, keys):
#         h = self.get_harsh(keys)
#         for element in self.arr[h]:# to iterate it element and key in same point
#             if  element[0] == keys:# if 0 position key match with key to seach then enter in loop
#                 return element[1]#get element that
#
#     def __setitem__(self, key, value):
#         h = self.get_harsh(key)
#         found = False
#         for idx,element in enumerate(self.arr[h]):
#             if len(element) == 2 and element[0] == key:
#                 self.arr[h][idx] = (key,value)
#                 found = True
#                 break
#             if not found:
#                 self.arr[h].append((key,value))
#
#     def __delitem__(self, key):
#         h = self.get_harsh(key)
#         for index, element in enumerate(self.arr[h]):
#             if element[0] == key:
#                 del self.arr[h][index]
#
#
# t = Harsh_Table()
# print(t.get_harsh('march 6'))
# t['march 6']= 120
# t['march 17']= 1120
# del t["march 17"]
# t['march 19']= 1290
# t['march 18']= 100
# print(t['march 6'])
# print(t.arr)
# print(t['march 17'])
# print(t.get_harsh('march 6'))


#=-----------------------------------------------Pratice-------------------------------------------------(
# arr = []
#
# with open('nyc_weather.csv','r') as f:
#     for line in f:
#         token = line.split(',')
#         try:
#             temperature = int(token[1])
#             arr.append(temperature)
#         except:
#             print("Invalide temperature.Ignore the row")
#
# print(arr)
# tt = sum(arr[0:7])
# xx = len(arr[0:7])
# print(tt/xx)
# print(arr[0:10])


#--------------------------------------------Practice---------------------------------------------------
weather_dict = {}

with open('nyc_weather.csv','r') as f:
    for line in f:
        token = line.split(',')
        day = token[0]
        try:
            #tt = int(token[1])
            weather_dict[day]= int(token[1])
        except:
            print("invalid")


print(weather_dict)
print(weather_dict['Jan 2'])
