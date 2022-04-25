ctp = float(input("Insira a nota da componente CTP:\n"))
cp = float(input("Insira a nota da componente CP:\n"))
media = int((ctp*0.36)+(cp*0.64))
if ((ctp<6.5) or (cp<6.5)):
        media = 66
if (media<10):
    atpr = float(input("Insira a nota de recurso ATPR:\n"))
    apr = float(input("Insira a nota de recurso APR:\n"))
    apa = float(input("Insira a nota da componente APA:\n")) #APA ERA NECESSARIA PARA CALCULAR A MEDIA EM CASA DE RECURSO
    media = int((0.36*max(ctp,atpr)+0.64*max(cp,apr,(1/4)*apa+(3/4)*apr)))
    if ((atpr<6.5) or (apr<6.5) or (apa<6.5)):
        media = 66
print ("A sua média é:", media)
