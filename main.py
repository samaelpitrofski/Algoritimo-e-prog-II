
from Estado import Estado
from Cidade import Cidade

import csv



#MENU - 1
def estadoscadstrado():
    print("...Estados Cadastradas...")
    for p in lstEstados:
        print('-->', p.nome.ljust(30), '- UF:', p.sigla)

def cad_nomestad():
    estadoscadstrado()
    while True:
        estados = input('Digite o nome do estado: ')
        return estados.upper()



def cad_sigla():
    while True:
        sigla = input('Digite a sigla do estado: ')
        if sigla:
            return sigla.upper()
        else:
            print('É obrigatório preencher esses dados..')
            return cad_sigla()

def cad_estados():
    print('=-=-=-= Cadastrar Estados')
    estados = Estado(cad_nomestad(), cad_sigla())
    lstEstados.append(estados)





#===============================================================================================================================================
# MENU - 2
def cad_nomecidade():
    while True:
        cidade = input('Digite o nome da Cidade:')
        if cidade:
            return cidade.upper()
        else:
            print('É obrigatório preencher esses dados..')
            return cad_nomecidade()



def cad_ufcidade():
    for p in lstEstados:
        print(p.sigla)
    while True:

        ufcidade = input('Digite o UF correspondente: ')
        if ufcidade:
                if ufcidade.upper() in p.sigla:
                    return ufcidade.upper()
                else:
                    print("O UF digitado não está cadastrado.")
                    return cad_ufcidade()
        else:
            return cad_ufcidade()

def cad_cidade():
    cidade = Cidade(cad_nomecidade(),cad_ufcidade())
    lstCidades.append(cidade)


#===============================================================================================================================================
# MENU - 3  
def relatorio_estados():
    print("...Estados Cadastradas...")
    for p in lstEstados:
        print('-->',p.nome.ljust(30),'- Total de Vacinado:',p.qt_estado)
    input("[ENTER] Retorna ao menu.")


#===============================================================================================================================================
# MENU - 4 
def relatorio_cidades():
    print("...Cidades Cadastradas...")
    for p in lstCidades:
        print('-->', p.nome.ljust(30), '- Total de Vacinado:', p.qt_casos)
    input("[ENTER] Retorna ao menu.")


#===============================================================================================================================================
# MENU - 5 

def at_casos():
    print('=-=-=-=-=Atualizar números de Vacinados nas Cidades')
    print('=-=-=-=-=Selecione a cidade pelo indice')
    for ind, cidade in enumerate(lstCidades):
        print(f'[{ind}] -- {cidade.nome}')
    index = int(input('>>> Digite o índice: '))
    cidade_index= lstCidades[index]
    atua_vacina = int(input('>>> Digite numero de vacinados: '))
    if atua_vacina >= 0:
        cidade_index.atuVacina_cidades(atua_vacina)
        for ind, estado in enumerate(lstEstados):
            if estado.getSiglaEstados() == cidade_index.getSiglaCidade():
                estado.atuVacina_estados(atua_vacina)
    else:
        print('O número de vacinas digitados não podem ser negativos.')

#===============================================================================================================================================
# MENU - 6

def salvar_relatorio():

    with open ('Relatorio_estado.csv', 'w', newline= '') as arquivo:
        wr = csv.writer(arquivo)
        for p in lstEstados:
            wr.writerow((p.nome.ljust(30),'- Total de Vacinados:',p.qt_estado))

    with open ('Relatorio_cidade.csv', 'w', newline= '') as arquivo:
        wr = csv.writer(arquivo)
        for p in lstCidades:
            wr.writerow(( p.nome.ljust(30),'- Total de Vacinado:', p.qt_casos))

    print ('Os relatórios foram gerados com sucesso')
    input("[ENTER] Retorna ao menu.")



#===============================================================================================================================================


lstEstados = []
lstCidades = []



#Programa Principal
while True:

    menu = """
    +--------------------------------------------+
    |Menu                                        |
    +--------------------------------------------+
    |   0- Finalizar                             |
    |   1- Cadastrar Estados                     |
    |   2- Cadastrar Cidades                     |
    |   3- Relatório de Estados                  |
    |   4- Relatório de Cidades                  |
    |   5- Atualizar número de Vacinado          |   
    |   6- Salvar em aqruivos                    | 
    +--------------------------------------------+
    Escolha:""" 

    escolha = input(menu)

    if escolha == '0':
        print("...O programa foi encerrado....")
        break

    if escolha == '1':
        cad_estados()

    if escolha == '2':
        cad_cidade()

    if escolha == '3':
        relatorio_estados()
        
    if escolha == '4':
        relatorio_cidades()

    if escolha == '5':
        at_casos()

    if escolha == '6':
        salvar_relatorio()