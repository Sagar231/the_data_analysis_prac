
 #[1,2,34,4]
#add
# append 

# mylist.append(90)  #append basially adds "whatever you give" at the end of the list
# mylist.append(10)
#   #[1,2,34,4,90,10]
# mylist.append(30)
#   #[1,2,34,4,90,10,30]
   
# #insert   (index, value)
# mylist.insert(2,24)
# print(mylist)
# # [1,2,24,34,4,90,10,30]
# #remove

# #pop()

# mylist.pop()
# print(mylist)

# mylist.pop(3)
# print(mylist)
# # [1, 2, 24, 4, 90, 10]
# #remove

# mylist.remove(4)
# print(mylist)
# print(type(mylist))

# '''
# slicing

# [start : end : step]
# range(start : end : step)
# '''
mylist = [1,2,56, 9 ,34,4]
print(mylist)

mylist.sort(reverse = True)

print(mylist)

yourlist = [0,-3,4,5,6,-6,9,-12,56,890,-356]
mylist = []
for i in yourlist:
    if i > 0 :
        mylist.append(i)
print(mylist)  