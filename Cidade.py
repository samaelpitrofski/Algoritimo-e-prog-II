class Cidade ():
    def __init__ (self,nome,estado,qt_casos = 0):
        self.nome = nome
        self.estado = estado
        self.qt_casos = qt_casos

    def setSiglaCidade(self, estado):
        self.estado = estado

    def getSiglaCidade(self):
        return self.estado

    def atuVacina_cidades (self, newQTvacinados):
        self.qt_casos += newQTvacinados

    def __str__(self):
        return "...Cidade: "+self.nome+  " Estado: "+self.estado+ " Casos: "+str(self.qt_casos)