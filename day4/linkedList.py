class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#setting the data (linked list consist of 3 important part first the 'data' than the 'next address' and the 'current address')
node1=Node(10)
node2=Node(200)
node3=Node(2000)
node4=Node(23)

#link all the nodes together

node1.next=node2# here i guess the node2 stores the current address of node2
node2.next=node3
node3.next=node4

#print all the linked list

cuurent_address=node1 #here i first used the node1 address to make the train running

while (cuurent_address != None):
    print(cuurent_address.data ,'>')
    cuurent_address=cuurent_address.next
print(None)
#----------------------------------------leetcode two sums-------------------------------
# def twoSum(nums, target):
#         empty_array = []
#         left = 0
#         right = len(nums) - 1
#         while(left < right):
#                 tempSum = nums[left] + nums[right]
#                 if tempSum == target:
#                     return list(map(int,[left,right]))
#                 elif tempSum > target:
#                         right -= 1
#                 elif tempSum < target:
#                        left += 1 
        
#         return list((-1,-1))

# def fact(n):   
#     return n*(fact(n-1))

# num=fact(5)

# print(num)


# suupose=[2,3,6,8]
# nums_array = [3,3]
# target = 6
# result = twoSum(nums=nums_array,target=target)
# print(result)           

