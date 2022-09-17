greet=input('').lower().replace(" ","")
if(greet=='hello'):
    money=0
elif(greet[0:5]=='hello'):
    money=0
elif(greet[0]=='h'):
    money=20
else :
    money=100

print ('$',money)

