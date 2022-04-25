def listajogos(listaequipas):
    listajogos=[]
    for equipa1 in listaequipas:
        for equipa2 in listaequipas:
            if equipa1==equipa2:
                continue
            listajogos.append((equipa1,equipa2))
    return listajogos

def main():
    print("Introduza as equipas de futebol do campeonato:")
    listaequipas=[]
    while True:
        equipa=input()
        if (equipa==''):break
        listaequipas.append(equipa)
    jogostemporada = (listajogos(listaequipas))
    print('Jogos:', jogostemporada)
    print('Insira os resultados (__,__):')
    dic_resultado={}
    for jogo in jogostemporada:
        print(jogo[0],'vs',jogo[1],':')
        resultado=input()
        dic_resultado.setdefault(jogo, resultado)
        #fiquei no 4D
main()