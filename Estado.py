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

    def atuVacina_estados (self, newQTvacinados):
        self.qt_estado += newQTvacinados

    def __str__(self):
        return "...Estado: "+self.nome+  " UF: "+self.sigla+  " País: "+self.pais+ " Quantidade: "+str(self.qt_estado)
