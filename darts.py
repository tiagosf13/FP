# You throw a dart that hits coordinates (x, y) on a dartboard.
# Create a program that gives you the score.
# See:
#   https://en.wikipedia.org/wiki/Darts#Dartboard
#   https://www.dimensions.com/element/dartboard

from math import atan, degrees, sqrt
print("Enter the coordinates in mm from the center of the board.")
x = float(input("x? "))
y = float(input("y? "))
distancia = sqrt(((x)**2)+((y)**2))
print ("d", distancia)
# Points of the sectors, clockwise from the top
# Example: the sector right from the center is POINTS[5] == 6.
POINTS = (20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5)

# COMPLETE...
if (distancia<=170):
    if (x!=0) and (y!=0):
        declive = (y/x)
        angulo = degrees((atan(declive)))
        def subsetor(score):
            if (distancia<6.35) and (distancia>=0):   # ......FEITO.....PROXIMO PASSO SERIA TORNAR ISTO UMA FUNÇÃO PARA TORNAR O ALGORITMO MAIS EFICIENTE
                score = 50
            elif (6.35<distancia<16):
                score = 25
            elif (99<distancia<107):
                score = (3*score)
            elif (162<distancia<170):
                score = (2*score)
            return (score)

        if (angulo == -9,-27,-45,-63,-81,-99,-117,-135,-153,-171,171,153,135,117,99,81,63,45,27,9):
            score = 0
        elif (x<0) and (y<0):
            angulo = (angulo-180)
        elif (x<0) and (y>0):
            angulo = (angulo-180)
        print ("ang", angulo)
        if (-9<angulo<9): # SETOR 6 pontuação apenas para 4 zonas, pois as restantes sao de pontuação 6
            score = (POINTS[5]) # 6
            subsetor(score)
        elif (-27<angulo): # SETOR 10
            score = (POINTS[6]) # 10
            subsetor(score)
        elif (-45<angulo): # SETOR 15
            score = (POINTS[7]) # 15
            subsetor(score)
        elif (-63<angulo): # SETOR 2
            score = (POINTS[8]) # 2
            subsetor(score)
        elif (-81<angulo): # SETOR 17
            score = (POINTS[9]) # 17
            subsetor(score)
        elif (-99<angulo): # SETOR 3
            score = (POINTS[10]) # 3
            subsetor(score)
        elif (-117<angulo): # SETOR 19
            score = (POINTS[11]) # 19
            subsetor(score)
        elif (-135<angulo): # SETOR 7
            score = (POINTS[12]) # 7
            subsetor(score)
        elif (-153<angulo): # SETOR 16
            score = (POINTS[13]) # 16
            subsetor(score)
        elif (-171<angulo): # SETOR 8
            score = (POINTS[14]) # 8
            subsetor(score)
        elif (171<angulo): # SETOR 11
            score = (POINTS[15]) # 11
            subsetor(score)
        elif (153<angulo): # SETOR 14
            score = (POINTS[16]) # 14
            subsetor(score)
        elif (135<angulo): # SETOR 9
            score = (POINTS[17]) # 9
            subsetor(score)
        elif (117<angulo): # SETOR 12
            score = (POINTS[18]) # 12
            subsetor(score)
        elif (99<angulo): # SETOR 5
            score = (POINTS[19]) # 5
            subsetor(score)
        elif  (81<angulo): # SETOR 20
            score = (POINTS[0]) # 20
            subsetor(score)
        elif (63<angulo): # SETOR 1
            score = (POINTS[1]) # 1
            subsetor(score)
        elif (45<angulo): # SETOR 18
            score = (POINTS[2]) # 18
            subsetor(score)
        elif (27<angulo): # SETOR 4
            score = (POINTS[3]) # 4
            subsetor(score)
        else: #elif (9<angulo): # SETOR 13
            score = (POINTS[4]) # 13
            subsetor(score)
    elif (x==0) and (y==0):
        score = 50
    elif (x==0) and (y!=0):
        if (y>0):
            score = 20
        else:
            score = 3
    elif (x>0): # PASSOU DE ELSE/IF PARA ELIF, PARECE FUNCIONAR ATÉ AO MOMENTO
        score = 6
    else:
        score = 11
    print(score)
else: 
    print ("As coordenadas não existem")
