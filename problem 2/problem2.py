a=int(input("Enter the total number of classes:"))
b=int(input("Enter the number of classes attended:"))
percentage=(b/a)*100
if (percentage>=75):
 print("Status:Eligible")
else:
 print("Status:Not Eligible")
m=((75-percentage)*a)/100
print("Additional classes required:",m)
