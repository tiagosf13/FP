tempocam = ((10*1)+(3*6)+(4*10))
horarest= (tempocam//60) #tirar os 60 minutos aos 68(tempocam)
minurest = (tempocam%60) #tirar o resto dos 68-60=8
minu = (52+minurest)
if (minu ==60):
    minu = ("00")
hora = (7+horarest)

print (hora,":",minu) 
