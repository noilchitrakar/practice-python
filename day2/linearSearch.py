# a=[2,4,5,7,8]
# f=int(input("enter the number you want to search"))
# for x in range(len(a)):
#     if f==a[x]:
#         print(f"number found at position{x+1}")

def linearSearch(a):
    f=int(input("enter the number you want to search"))
    for x in range(len(a)):
        if f==a[x]:
            return x
    return -1

a=[2,4,5,7,8]
value=linearSearch(a)

if value!=-1:
    print(f"number found at index {value+1}")
else:
    print("number not found")




