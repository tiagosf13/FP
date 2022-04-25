lst = ["A", "B", "C", "D", "E", "F", "G", "H"]
lstnum = [1, 2, 3, 4, 5, 6, 7, 8]
lstcoordenadas={}
u = 0
lst[u]: "" for n in lst:
    lstcoordenadas.setdefault(lst[u], lstnum[u])
    
    u += 1
print(lstcoordenadas)