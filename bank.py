greet=input(' ').title()
x=greet[0:5]
if(greet=='Hello'):
    money=0
elif(x=='Hello'):
    money=0
elif(greet[0]=='H'):
    money=20
else :
    money=100

print ('$',money)
