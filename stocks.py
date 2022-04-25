
# Constantes para indexar os tuplos:
NAME,DATE,OPEN,MAX,MIN,CLOSE,VOLUME = 0,1,2,3,4,5,6

def main():
    lst = loadStockFile("nasdaq.csv")
    # Show just first and last tuples:
    print("first:", lst[0])
    print("last:", lst[-1])
    print(lst)

    print("a) totVol=", totalVolume(lst))

    print("b) maxVal=", maxValorization(lst))
    
    stocksDic = stocksByDateByName(lst)
    print("c) CSCO@11:", stocksDic['2020-10-12']['CSCO'])
    print("c) AMZN@22:", stocksDic['2020-10-22']['AMZN'])

    port = {'NFLX': 100, 'CSCO': 80}
    print("d) portfolio@01:", portfolioValue(stocksDic, port, "2020-10-01"))
    print("d) portfolio@30:", portfolioValue(stocksDic, port, "2020-10-30"))

def loadStockFile(filename):
    lst = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split('\t')
            name = parts[NAME]
            date = parts[DATE]
            tup = (name, date, float(parts[OPEN]), float(parts[MAX]),
                float(parts[MIN]), float(parts[CLOSE]), int(parts[VOLUME]))
            lst.append(tup)
    return lst

def totalVolume(lst):
    totVol = {}
    lista = set()
    n=0
    soma=0
    # COMO FAZER PARA POR AUTUMATICAMENTE COM O SET DE EMPRESAS
    while lst[n][NAME] == 'CSCO':
            soma+=soma + lst[n][VOLUME]
            n+=1
    totVol.setdefault('CSCO',soma)
    
    while lst[n][NAME] == 'TSLA':
            soma+=soma + lst[n][VOLUME]
            n+=1
    totVol.setdefault('TSLA',soma)
    
    while lst[n][NAME] == 'NFLX':
            soma+=soma + lst[n][VOLUME]
            n+=1
    totVol.setdefault('NFLX',soma)
    
    while lst[n][NAME] == 'QCOM':
            soma+=soma + lst[n][VOLUME]
            n+=1
    totVol.setdefault('QCOM',soma)
    
    while lst[n][NAME] == 'VOD':
            soma+=soma + lst[n][VOLUME]
            n+=1
    totVol.setdefault('VOD',soma)
    
    while lst[n][NAME] == 'EA':
            soma+=soma + lst[n][VOLUME]
            n+=1
    totVol.setdefault('EA',soma)
    
    while lst[n][NAME] == 'ERIC':
            soma+=soma + lst[n][VOLUME]
            n+=1
    totVol.setdefault('ERIC',soma)
    
    while lst[n][NAME] == 'INTC':

            soma+=soma + lst[n][VOLUME]
            n+=1
    totVol.setdefault('INTC',soma)
    
    while lst[n][NAME] == 'AMZN':
            soma+=soma + lst[n][VOLUME]
            n+=1
    totVol.setdefault('AMZN',soma)
    
    while lst[n][NAME] == 'PTI':
            soma+=soma + lst[n][VOLUME]
            n+=1
    totVol.setdefault('PTI',soma)
    
    for name in lst:
        lista.add(name[0])
        
    lista = frozenset(lista)
    
    print(lista)
    return totVol

def maxValorization(lst):
    vMax = {}
    # Complete ...
    # EMPRESA,DATA,OPEN,CLOSE,VDR = 0,1,2,3,4
    n = 0
    novalista = []
    for elemento1 in lst:
        vdr = (lst[n][CLOSE]/lst[n][OPEN])*100
        novalista.append((lst[n][NAME],lst[n][DATE],lst[n][OPEN],lst[n][CLOSE],vdr))
        print('EMPRESA:',lst[n][NAME],'DATA :',lst[n][DATE],'OPEN:',lst[n][OPEN],'CLOSE:',lst[n][CLOSE], 'VALORIZAÇÃO DIÁRIA RELATIVA:', vdr)
        n += 1
    print(novalista)
    
    for elemento in novalista:
        n = 0
        if novalista[n][0]==novalista[n+1][0]:
            while novalista[n][0]==lst[n+1][0] and n<=len(novalista):
                if novalista[n][4]<novalista[n+1][4]:
                    valorizacao = novalista[n+1][4]
                else:
                    valorizacao = novalista[n][4]
                n += 1
            vMax.setdefault(novalista[n][1],(novalista[n][0],valorizacao))
        else:
            n += 1
            while novalista[n][0]==lst[n+1][0] and n<=len(novalista):
                if novalista[n][4]<novalista[n+1][4]:
                    valorizacao = novalista[n+1][4]
                else:
                    valorizacao = novalista[n][4]
                n += 1
            vMax.setdefault(novalista[n][1],(novalista[n][0],valorizacao))     
    
    return vMax

def stocksByDateByName(lst):
    dic = {}
    # Complete ...

    return dic

def portfolioValue(stocks, portfolio, date):
    assert date in stocks
    val = 0.0
    # Complete ...

    return val

if __name__ == "__main__":
    main()