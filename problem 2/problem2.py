n=int(input("Enter the number of classes attended out of 70 classes:"))
percentage=(n/70)*100
if (percentage>=75):
 print("Status:Eligible")
else:
 print("Status:Not Eligible")
m=(70-n)/2
print("Additional classes required:",m)
