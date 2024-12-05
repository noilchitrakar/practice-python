# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,
# # 1. In Feb, how many dollars you spent extra compare to January?
# # 2. Find out your total expense in first quarter (first three months) of the year.
# # 3. Find out if you spent exactly 2000 dollars in any month
# # 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# # 5. You returned an item that you bought in a month of April and
# # got a refund of 200$. Make a correction to your monthly expense list
# # based on this

expense={
    'January':2200,
    'February':2350,
    'March':2600,
    'April':2130,
    'May':2190
}
print("question 1")
print(expense['February']-expense['January'])

print("question 2")

count=0
Sum=0
for key,value in expense.items():
    count+=1;
    Sum+=value;
    # print(Sum)
    if(count==3):
        break
print(f"your total expense in first quarter (first three months) of the year is {Sum}")

print("question 3")
for value in expense.values():
    if value==2000:
        print("exacty 2000 spend")

print("question 4")
expense["June"]=1980

print(expense)


print("question 5")
expense["April"]=2130-200

print(expense)

# print(dir(list))
