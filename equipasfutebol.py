def Jogos(listaEquipas):
   assert len(listaEquipas) >= 2
   lista = []
   for eq1 in listaEquipas:
      for eq2 in listaEquipas:
         if eq1 == eq2:
            continue
         lista.append((eq1, eq2))
   return lista

def perguntarResultados(listaJogos, listaResultados):
    print('Introduz os resultados dos jogos separados por vírgulas')
    print('Exemplo: "0,0"')
    for jogo in listaJogos:
        res1, res2 = input(f'Introduz o resultado do jogo {jogo}: ').split(',')
        res1, res2 = int(res1), int(res2)
        listaResultados[jogo] = (res1, res2)

def main():
    print('Introduz os nomes das equipas, uma de cada vez, e carrega no Enter quando terminares.')
    listaEquipas = []
    listaResultados = {}
    while True:
        equipasInput = input('')
        if equipasInput == '':
            break
        listaEquipas.append(equipasInput.strip())
    listaJogos = Jogos(listaEquipas)
    perguntarResultados(listaJogos, listaResultados)
    print(listaResultados)
main()