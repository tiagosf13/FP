sec = int(input("Insira o tempo, em segundos, a ser formatado:\n"))
minu = (sec//60)
rsec = (sec%60)
horas = (minu//60)
rminu = (minu%60)
dias = (horas//24)
rhoras = (horas%24)
message= """
{}:{}:{}:{}
"""
print (message.format (dias ,rhoras, rminu, rsec))
