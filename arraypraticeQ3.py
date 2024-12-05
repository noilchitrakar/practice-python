# // Create a list of all odd numbers between 1 and a max number. 
# // Max number is something you need to take from a user using input() function



num=int(input("enter the max number you want to print at"))
#odd=[]
# for x in range(1,num,2):
#     odd.append(x)
#print(odd)
#or
odd=[x for x in range(1,num,2)]

print(odd)