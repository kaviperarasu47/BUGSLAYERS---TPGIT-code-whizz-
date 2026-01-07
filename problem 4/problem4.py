income=int(input("Enter the income:"))
transport=int(input("Enter the transport expenses:"))
food=int(input("Enter the food expenses:"))
house=int(input("Enter the household expenses:"))
if (transport>food & transport>house):
    print("Transport has the highest expenses")
elif(food>house):
    print("Food has the highest expenses")
else:
    print("House has the highest expenses")
total=transport+house+food
bal=income-total
print("The total expense is",total)
print("The balance is",bal)