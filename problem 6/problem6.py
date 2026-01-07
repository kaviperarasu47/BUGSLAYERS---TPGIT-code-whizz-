p=input("Enter the password:")
point=1
special=[!,@,#,$,%,&]
l=len(p)
if (l>=8):
    point+=1
if (isupper(p)):
    point+=1
if(islower(p)):
    point+=1
if(isnumerical(p)):
    point+=1
for i in special:
if (p=i):
 point+=1
if point<=2:
print("Password is weak")
if point<=4:
print("Password is medium")
if points=5:
print("password is strong")
