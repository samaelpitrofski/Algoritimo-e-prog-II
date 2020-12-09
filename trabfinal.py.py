# Trabalho Final
#Classes
class Estado():
    def __init__ (self,nome,sigla):
        self.nome = nome
        self.sigla = sigla
        self.pais = 'Brasil'
        self.qt_estado = 0

    def setSiglaEst (self, sigla):
        self.sigla = sigla

    def getSiglaEstados(self):
        return self.sigla

    def getNomeEst(self):
        return self.nome

    def atuCasos_estados (self, newQTcasos):
        self.qt_estado += newQTcasos

    def __str__(self):
        return "...Estado: "+self.nome+  " UF: "+self.sigla+  " País: "+self.pais+ " Quantidade: "+str(self.qt_estado)

#===============================================================================================================================================

class Cidade ():
    def __init__ (self,nome,estado,qt_casos = 0):
        self.nome = nome
        self.estado = estado
        self.qt_casos = qt_casos

    def setSiglaCidade(self, estado):
        self.estado = estado

    def getSiglaCidade(self):
        return self.estado

    def atuCasos_cidades (self, newQTcasos):
        self.qt_casos += newQTcasos

    def __str__(self):
        return "...Cidade: "+self.nome+  " Estado: "+self.estado+ " Casos: "+str(self.qt_casos)



#===============================================================================================================================================
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
        print('-->',p.nome.ljust(30),'- Total de casos:',p.qt_estado)
    input("[ENTER] Retorna ao menu.")


#===============================================================================================================================================
# MENU - 4 
def relatorio_cidades():
    print("...Cidades Cadastradas...")
    for p in lstCidades:
        print('-->', p.nome.ljust(30), '- Casos registrados:', p.qt_casos)
    input("[ENTER] Retorna ao menu.")


#===============================================================================================================================================
# MENU - 5 

def at_casos():
    print('=-=-=-=-=Atualizar números de casos nas Cidades')
    print('=-=-=-=-=Selecione a cidade pelo indice')
    for ind, cidade in enumerate(lstCidades):
        print(f'[{ind}] -- {cidade.nome}')
    index = int(input('>>> Digite o índice: '))
    cidade_index= lstCidades[index]
    atua_casos = int(input('>>> Digite numero de casos: '))
    if atua_casos >= 0:
        cidade_index.atuCasos_cidades(atua_casos)
        for ind, estado in enumerate(lstEstados):
            if estado.getSiglaEstados() == cidade_index.getSiglaCidade():
                estado.atuCasos_estados(atua_casos)
    else:
        print('O número de casos digitados não podem ser negativos.')



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
    |   5- Atualizar número de casos             | 
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


        