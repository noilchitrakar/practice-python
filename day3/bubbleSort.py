a=[100,2,13,8,9,23,6,2,22,45,67]

# a.sort()

# print(a)
# print(len(a))
print("-----------bubble sort-----------")
for i in range(len(a)):
    print("1st loop--")
    for j in range(len(a)-i-1):
        print("2nd loop-------")
        temp=a[j]
        if (a[j]>a[j+1]):
            a[j]=a[j+1]
            a[j+1]=temp
print(a)