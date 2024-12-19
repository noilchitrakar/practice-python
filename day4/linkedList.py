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
      

