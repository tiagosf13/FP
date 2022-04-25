import os
from datetime import datetime
from random import randrange


def codigo():
    codigo_emprestimo=str(randrange(1000000000,9999999999))
    if carregar_ficheiro_emprestimos()==[]:
        return codigo_emprestimo
    else:
        for element in carregar_ficheiro_emprestimos():
            if element[6]==codigo_emprestimo:
                return codigo()
            else:
                return codigo_emprestimo
        

def resolver_emprestimo(lista_emprestimos,wallet_list):
    if lista_emprestimos==[]:
        print('---------------------------')
        print('Não tem empréstimos')
        print('---------------------------')
        main()
    kill=0
    for element in lista_emprestimos:
        if element[5]=='Resolvido':
            kill=1
        else:
            kill=0
    if kill==1:
        print('-----------------------------------------')
        print('Não tem nenhum empréstimo por resolver')
        print('-----------------------------------------')
        main()
    print('----------------------------------------------------------------------------------------EMPRESTAR CRÉDITOS----------------------------------------------------------------------------------------')
    print('')
    print('{:>20} {:^5} {:^20} {:^5} {:^20} {:^5} {:^20} {:^5} {:^16} {:^5} {:>15} {:>12} {:>15}'.format('DATA DO EMPRÉSTIMO','|','MOEDA','|','QUANTIDADE','|','VALOR EMPRESTADO','|','PESSOA','|','CÓDIGO','|','SITUAÇÃO'))
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    for element in lista_emprestimos:
        print('{:>20} {:^5} {:^20} {:^5} {:^20} {:^5} {:^20} {:^5} {:^16} {:^5} {:>17} {:>10} {:>17}'.format(element[0],'|',element[1],'|',element[2],'|',element[3],'|',element[4],'|',element[6],'|',element[5]))
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('')
    print('USE 999 PARA VOLTAR ATRÁS')
    print('')
    codigo_utilizador=input('Insira o código do empréstimo a ser resolvido:\n')
    if codigo_utilizador=='999':
        os.system('cls')
        main()
    for element in lista_emprestimos:
        data=element[0]
        moeda=element[1]
        quantidade=element[2]
        valor=element[3]
        pessoa=element[4]
        codigo=element[6]
    if codigo_utilizador==codigo:
        print('---------------------------------------------------')
        print('Empréstimo:')
        print('Data: ',data)
        print('Moeda: ',moeda)
        print('Quantidade: ',quantidade)
        print('Valor do Empréstimo: ',valor)
        print('Pessoa: ',pessoa)
        print('Código: ',codigo)
        print('---------------------------------------------------')
        file='wallet.txt'
        for element in wallet_list:
            if element[0]==str(moeda):
                quantidade_inicial=element[1]
        quantidade_emprestimo_int=int(moeda)*int(quantidade)
        quantidade_modificada=quantidade_emprestimo_int+quantidade_inicial
        confirm=input('Deseja resolver este empréstimo?(Y/n)\n')
        if confirm=='Y':
            modificar_ficheiro(wallet_list,file,moeda,quantidade_modificada)
            int_moeda_emprestimo=int(moeda)
            int_quantidade_emprestimo=int(quantidade)
            total=int_moeda_emprestimo*int_quantidade_emprestimo
            total=str(total)
            tipo_operacao='adicionado(emprestimo pago)'
            quantidade_inicial_str=str(quantidade_inicial)
            quantidade_modificada_str=str(quantidade_modificada)
            append_new_line('transactions.txt',datetime.today().strftime('%Y-%m-%d %H:%M:%S') + ',' + str(moeda)+ ',' + quantidade+',' + quantidade_inicial_str + ',' + quantidade_modificada_str + ',' + total + ',' + tipo_operacao)
            file_emprestimos='emprestimos.txt'
            if modificar_ficheiro_emprestimos(carregar_ficheiro_emprestimos(),file_emprestimos,moeda,quantidade, pessoa,data,codigo):
                os.system('cls')
                print('-------------------------')
                print('Empréstimo Resolvido')
                print('-------------------------')
                main()
            else:
                print('Erro')

def modificar_ficheiro_emprestimos(lista_emprestimos,ficheiro,moeda_emprestimo,quantidade_emprestimo, pessoa,data_emprestimo,codigo_emprestimo): #funcao para modificar o ficheiro emprestimos apos qualquer tipo de operacao feita na carteira
    moeda_emprestimo_int=int(moeda_emprestimo)
    for element in lista_emprestimos:
        if (element[1]==moeda_emprestimo_int) and (element[2]==quantidade_emprestimo) and(element[4]==pessoa) and (element[0]==data_emprestimo) and(element[6]==codigo_emprestimo):
            element[5]='Resolvido'
    fileop=open(ficheiro,'w')
    for element in lista_emprestimos:
        fileop.write(str(element[0])+','+str(element[1])+','+str(element[2]+','+str(element[3])+','+str(element[4])+','+str(element[5])+','+str(element[6])+'\n'))
    for element in lista_emprestimos:
        if element[4]==pessoa:
            if element[1]==moeda_emprestimo_int:
                if element[2]==quantidade_emprestimo:
                    print(element[0])
                    print(data_emprestimo)
                    if element[0]==data_emprestimo:
                        return True

def ver_emprestimos(lista_emprestimos):
    os.system('cls')
    if lista_emprestimos==[]:
        print('------------------------------')
        print('Lista de empréstimos vazia')
        print('------------------------------')
        main()
    print('----------------------------------------------------------------------------------------EMPRÉSTIMOS-----------------------------------------------------------------------------------')
    print('')
    print('{:>20} {:^5} {:^20} {:^5} {:^20} {:^5} {:^20} {:^5} {:^16} {:^5} {:>15} {:>12} {:>15}'.format('DATA DO EMPRÉSTIMO','|','MOEDA','|','QUANTIDADE','|','VALOR EMPRESTADO','|','PESSOA','|','CÓDIGO','|','SITUAÇÃO'))
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    for element in lista_emprestimos:
        print('{:>20} {:^5} {:^20} {:^5} {:^20} {:^5} {:^20} {:^5} {:^16} {:^5} {:>17} {:>10} {:>17}'.format(element[0],'|',element[1],'|',element[2],'|',element[3],'|',element[4],'|',element[6],'|',element[5]))
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    main()


def carregar_ficheiro_emprestimos():
    lst=[]
    with open("emprestimos.txt") as file:
        for line in file:
            lst.append(line.strip().split(","))
    newlst=[]
    for element in lst:
        if element[0]!='':
            newlst.append(element)
    file_open=open('emprestimos.txt', 'w')
    for element in newlst:
        file_open.write(element[0]+','+element[1]+','+element[2]+','+element[3]+','+element[4]+','+element[5]+','+element[6]+'\n')
        element[1]=int(element[1])
    return newlst

def emprestimo(wallet_list):
    os.system('cls')
    print('------------------------EMPRESTAR CRÉDITOS------------------------')
    print('')
    print("{:^20} {:^5} {:^10} {:^5} {:^10}".format("TIPO DE MOEDA","|","QUANTIDADE ADQUIRIDA","|","TOTAL"))
    print("------------------------------------------------------------------")
    total_carteira=0
    for sublist in wallet_list:
        moeda=sublist[0]
        tipo_moeda=str(moeda)+'€'
        quantidade=sublist[1]
        total=float(moeda)*float(quantidade)
        total_carteira+=total
        y=str(total)+'€'
        print("{:^20} {:^5} {:^20} {:^5} {:^10}".format(tipo_moeda,"|", quantidade,"|", y))
        print("------------------------------------------------------------------")
    x=str(total_carteira)+'€'
    print('{:>20} {:^5} {:^20} {:^5} {:^10}'.format('','','TOTAL NA CARTEIRA','|',x))
    print("------------------------------------------------------------------")
    print('')
    print('USE 999 PARA VOLTAR ATRÁS')
    print('')
    moeda_emprestimo=input('Insira a moeda a ser sujeito a empréstimo:\n')
    if moeda_emprestimo=='999':
        os.system('cls')
        main()
    valores=[]
    for element in wallet_list:
        valores.append(element[0])
    moeda_emprestimo_int=int(moeda_emprestimo)
    if moeda_emprestimo not in valores:
        emprestimo(carregar_ficheiro())
    print('')
    quantidade_emprestimo=input('Insira a quantidade a ser sujeito a empréstmo (se introduziu a moeda errada insira 555):\n')
    if quantidade_emprestimo=='555':
        os.system('cls')
        emprestimo(carregar_ficheiro())
    quantidade_emprestimo_int=int(quantidade_emprestimo)
    for element in wallet_list:
        if element[0]==moeda_emprestimo:
            if element[1]<quantidade_emprestimo_int:
                os.system('cls')
                print('-----------------------------------------------------')
                print('Não possui o crédito necessário para o empréstimo')
                print('-----------------------------------------------------')
                main()
    print('')
    pessoa_emprestimo=input('Insira a pessoa a quem se destina o empréstimo:\n')
    pessoa_emprestimo=pessoa_emprestimo[0].upper()+pessoa_emprestimo[1:]
    file='wallet.txt'

    for element in wallet_list:
        if element[0]==moeda_emprestimo:
            quantidade_inicial=int(element[1])
            if quantidade_emprestimo_int<=quantidade_inicial:
                quantidade_final=quantidade_inicial-quantidade_emprestimo_int
    moeda_int=int(moeda_emprestimo)
    quantidade_final_int=int(quantidade_final)
    valor=moeda_int*quantidade_emprestimo_int
    valor=str(valor)
    codigo_ficheiro_emprestimo=str(codigo())
    situacao_emprestimo='Por Resolver'
    append_new_line('emprestimos.txt',datetime.today().strftime('%Y-%m-%d %H:%M:%S')+','+ moeda_emprestimo +','+quantidade_emprestimo+','+valor+','+pessoa_emprestimo+','+situacao_emprestimo+','+codigo_ficheiro_emprestimo)
    os.system('cls')
    if modificar_ficheiro(wallet_list,file,moeda_emprestimo,quantidade_final)==True:
        valor='-'+valor
        transferencias(moeda_emprestimo,quantidade_emprestimo,quantidade_inicial,quantidade_final,valor,'removido(emprestimo)')
        print('-----------------------------------')
        print('Emprestado', valor,'€ a',pessoa_emprestimo)
        print('')
        print('Código do Empréstimo:',codigo_ficheiro_emprestimo)
        print('-----------------------------------')
    else:
        print('-------------------')
        print('Erro na transação')
        print('--------------------')
    return main()

def ver_extrato(lista_extrato):
    if lista_extrato==[]:
        print('---------------------')
        print('Extrato Vazio')
        print('---------------------')
        main()
    for element in lista_extrato:
        if 'removido' in element:
            element[5]='-'+element[5]
    os.system('cls')
    print('--------------------------------------------------------------------------------EXTRATO-------------------------------------------------------------------------------')
    print('')
    print('{:>20} {:^5} {:^20} {:^5} {:^20} {:^5} {:^20} {:^12} {:^10} {:^12} {:<5}'.format('DATA DA TRANSAÇÃO','|','MOEDA','|','QUANTIDADE TRANSFERIDA','|','QUANTIDADE INICIAL','|','QUANTIDADE FINAL','|','TOTAL DA OPERAÇÃO'))
    print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    for element in lista_extrato:
        print('{:>20} {:^5} {:^20} {:^5} {:^20} {:^10} {:^20} {:^5} {:^20} {:^12} {:>10}'.format(element[0],'|',element[1],'|',element[2],'|',element[3],'|',element[4],'|',element[5]+'€'))
        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    for element in lista_extrato:
        if '9999999999999999' in element:
            decisao=1
        else:
            decisao=0
    if decisao==1:
        print('______________________________________________________________')
        print('O código 9999999999999999 representa um RESET da carteira')
        print('______________________________________________________________')
    main()

def carregar_ficheiro_extrato():
    lst=[]
    with open("transactions.txt") as file:
        for line in file:
            lst.append(line.strip().split(","))
    if lst==[]:
        os.system('cls')
        return lst
    for element in lst:
        element[1]=int(element[1])
    return lst

def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)

def transferencias(moeda,quantidade,quantidade_inicial,quantidade_modificada,total,tipo_operacao):
    filetrans='transactions.txt'
    filetransedit=open(filetrans, 'a+')
    string_moeda=str(moeda)
    string_quantidade=str(quantidade)
    string_quantidade_inicial=str(quantidade_inicial)
    string_quantidade_modificada=str(quantidade_modificada)
    string_total=str(total)
    append_new_line('transactions.txt',datetime.today().strftime('%Y-%m-%d %H:%M:%S') + ',' + string_moeda+ ',' + string_quantidade +',' + string_quantidade_inicial + ',' + string_quantidade_modificada + ',' +string_total + ',' + tipo_operacao)
    filetransedit.close()

def carregar_ficheiro(): #funcao para carregar o ficheiro, e converte lo para uma lista
    lst=[]
    with open("wallet.txt") as file:
        for line in file:
            lst.append(line.strip().split(","))
    for element in lst:
        element[1]=int(element[1])
    return lst

def ver_Carteira(wallet_list): #funcao para apresentar os fundos da carteira formatados ao utilizador
    os.system('cls')
    print('---------------------------VER CARTEIRA---------------------------')
    print("{:^20} {:^5} {:^10} {:^5} {:^10}".format("TIPO DE MOEDA","|","QUANTIDADE ADQUIRIDA","|","TOTAL"))
    print("------------------------------------------------------------------")
    total_carteira=0
    for sublist in wallet_list:
        moeda=sublist[0]
        tipo_moeda=str(moeda)+'€'
        quantidade=sublist[1]
        total=float(moeda)*float(quantidade)
        total_carteira+=total
        y=str(total)+'€'
        print("{:^20} {:^5} {:^20} {:^5} {:^10}".format(tipo_moeda,"|", quantidade,"|", y))
        print("------------------------------------------------------------------")
    x=str(total_carteira)+'€'
    print('{:>20} {:^5} {:^20} {:^5} {:^10}'.format('','','TOTAL NA CARTEIRA','|',x))
    print("------------------------------------------------------------------")
    return (main())

def adicionar_creditos(wallet_list): #funcao para adicionar creditos
    os.system('cls')
    print('---------------------------------------------ADICIONAR CRÉDITOS-----------------------------------------')
    print('USE 999 PARA VOLTAR ATRÁS')
    print('')
    moeda=input('Que tipo de moeda deseja adicionar?\n')
    lst_numerario=[]
    for element in wallet_list:
        lst_numerario.append(element[0])
    if moeda=='999':
        os.system('cls')
        main()
    elif moeda not in lst_numerario:
        print('---------------------------------------')
        print('Moeda não existe. TENTE OUTRA VEZ')
        print('---------------------------------------')
        adicionar_creditos(carregar_ficheiro())
    print('')
    print('')
    quantidade=input('Quantidade da moeda a ser adicionada(se introduziu a moeda errada insira B):\n')
    quantidade=quantidade.upper()
    if quantidade=='B':
        adicionar_creditos(carregar_ficheiro())
    file='wallet.txt'
    for element in wallet_list:
        if element[0]==moeda:
            quantidade_inicial=element[1]
    quantidade_modificada=int(quantidade)+int(quantidade_inicial)
    
    os.system('cls')
    if modificar_ficheiro(wallet_list,file,moeda, str(quantidade_modificada))==True:
        moedaint=int(moeda) 
        intquant=int(quantidade)
        transferencias(moeda,quantidade,quantidade_inicial,quantidade_modificada,intquant*moedaint,'adicionar')
        print('------------------------')
        print('Adicionado', intquant*moedaint,'€')
        print('------------------------')
    else:
        print('-------------------')
        print('Erro na transação')
        print('--------------------')
    return(main())

def remover_creditos(wallet_list):
    os.system('cls')
    print('-------------------------REMOVER CRÉDITOS-------------------------')
    print('')
    print("{:^20} {:^5} {:^10} {:^5} {:^10}".format("TIPO DE MOEDA","|","QUANTIDADE ADQUIRIDA","|","TOTAL"))
    print("------------------------------------------------------------------")
    total_carteira=0
    for sublist in wallet_list:
        moeda=sublist[0]
        tipo_moeda=str(moeda)+'€'
        quantidade=sublist[1]
        total=float(moeda)*float(quantidade)
        total_carteira+=total
        y=str(total)+'€'
        print("{:^20} {:^5} {:^20} {:^5} {:^10}".format(tipo_moeda,"|", quantidade,"|", y))
        print("------------------------------------------------------------------")
    x=str(total_carteira)+'€'
    print('{:>20} {:^5} {:^20} {:^5} {:^10}'.format('','','TOTAL NA CARTEIRA','|',x))
    print("------------------------------------------------------------------")
    print('')
    print('USE 999 PARA VOLTAR ATRÁS')
    print('')
    moeda=input('Que tipo de moeda deseja remover?\n')
    lst_numerario=[]
    for element in wallet_list:
        lst_numerario.append(element[0])
    if moeda=='999':
        os.system('cls')
        main()    
    elif moeda not in lst_numerario:
        remover_creditos(carregar_ficheiro())
    print('')
    quantidade=input('Quantidade da moeda a ser removida(se introduziu a moeda errada insira B):\n')
    quantidade=quantidade.upper()
    if quantidade=='B':
        remover_creditos(carregar_ficheiro())
    intquanti=int(quantidade)
    for element in wallet_list:
        if element[0]==moeda:
            if element[1]<intquanti:
                os.system('cls')
                print('----------------------------------------')
                print('Não possui esta quantidade de moedas')
                print('----------------------------------------')
                main()

    if quantidade=='555':
        remover_creditos(carregar_ficheiro())
    file='wallet.txt'
    for element in wallet_list:
        if element[0]==moeda:
            quantidade_inicial=element[1]
    inteiro_quantidade=int(quantidade)
    if inteiro_quantidade>quantidade_inicial:
        return 'ERRO: Saldo negativo'
    quantidade_modificada=int(quantidade_inicial)-int(quantidade)
    os.system('cls')
    if modificar_ficheiro(wallet_list,file,moeda, str(quantidade_modificada))==True:
        moedaint=int(moeda)
        intquant=int(quantidade)
        transferencias(moeda,quantidade,quantidade_inicial,quantidade_modificada,intquant*moedaint,'removido')
        print('-------------------')
        print('Removido', intquant*moedaint,'€')
        print('-------------------')
    else:
        print('-------------------')
        print('Erro na transação')
        print('-------------------')
    return(main())

def modificar_ficheiro(carteira,ficheiro,moeda,quantidade_modificada): #funcao para modificar o ficheiro wallet apos qualquer tipo de operacao feita na carteira
    for element in carteira:
        if element[0]==moeda:
            element[1]=quantidade_modificada
    fileop=open(ficheiro,'w')
    for element in carteira:
        fileop.write(str(element[0])+','+str(element[1])+'\n')
    for element in carteira:
        if element[0]==moeda:
            if element[1]==quantidade_modificada:
                return True
            else:
                return False
            
def reset_carteira(wallet_list):
    file='wallet.txt'
    for element in wallet_list:
        element[1]=0
    modificar_ficheiro(wallet_list, file, 0, 0)
    append_new_line('transactions.txt',datetime.today().strftime('%Y-%m-%d %H:%M:%S') + ',' + '9999999999999999'+ ',' + '9999999999999999'+',' + '9999999999999999' + ',' + '9999999999999999' + ',' + '' + ',' + '9999999999999999')
    os.system('cls')
    print('---------------------')
    print('CARTEIRA RESETADA')
    print('---------------------')
    
    return(main())

def main():
    print('__________________________________________________')
    print('MENU')
    print('__________________________________________________')
    print('1.Ver Carteira')
    print('')
    print('2.Adicionar crédito á Carteira')
    print('')
    print('3.Remover crédito á Carteira')
    print('')
    print('4.Empréstimo de Crédito')
    print('')
    print('5.Resolver Empréstimo')
    print('')
    print('6.Consultar Empréstimos')
    print('')
    print('7.Consultar Extrato')
    print('')
    print('8.Reset à Carteira')
    print('')
    print('0.Sair')
    print('__________________________________________________')
    escolha= input()
    print('__________________________________________________')
    lst_opcao_escolha=['0','1','2','3','4','5','6','7','8']
    if escolha=='1':
        ver_Carteira(carregar_ficheiro())
    if escolha=='2':
        adicionar_creditos(carregar_ficheiro())
    if escolha=='3':
        remover_creditos(carregar_ficheiro())
    if escolha=='4':
        os.system('cls')
        emprestimo(carregar_ficheiro())
    if escolha=='5':
        os.system('cls')
        resolver_emprestimo(carregar_ficheiro_emprestimos(),carregar_ficheiro())
    if escolha=='6':
        ver_emprestimos(carregar_ficheiro_emprestimos())
    if escolha=='7':
        ver_extrato(carregar_ficheiro_extrato())
    if escolha=='8':
        os.system('cls')
        print('---------------------RESET DA CARTEIRA---------------------')
        print('')
        confirm=input('Tem a certeza que deseja resetar a sua carteira?(Y/n):\n')
        if confirm=='Y':
            print(reset_carteira(carregar_ficheiro()))
        else:
            os.system('cls')
            main()
    if escolha=='0':
        os.system('cls')
        exit()
    if escolha not in lst_opcao_escolha:
        os.system('cls')
        main()
main()