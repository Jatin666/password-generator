import random
length=int(input("enter the length of password: "))
list1=[]
password=''
if(length<6):
    print("password should have atleast 6 characters")
    flag=False
elif(length>=6):
    for i in range(33,119):
        list.append(chr(i))
        flag=True
while(flag):
    randomCharacter = random.choice(list1)
    if(len(password) is length):
        break
    elif (randomCharacter not in password):
         password = password + (randomCharacter)
    else:
        continue
else:
 print("thank you")
print(password)