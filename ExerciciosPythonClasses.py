#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#-------------------------------------------------------------------------------
# -- Lista Classes -- 
#-------------------------------------------------------------------------------
print "-"*60+"\n1) Classe Bola: Crie uma classe que modele uma bola: \n\
Atributos: Cor, circunferência, material \n\
Métodos: trocaCor e mostraCor \n"+"-"*60
#-------------------------------------------------------------------------------
class Bola():
    def __init__(self,cor,circunferencia,material):
        self.cor=cor
        self.circunferencia=circunferencia
        self.material=material
    def trocarCor(self,novaCor):
        self.cor=novaCor
    def mostraCor(self):
        return self.cor
    def __str__(self):
        return "bola cor '%s', %.2f cm de %s"%(self.cor,self.circunferencia,self.material)

bol = Bola("Amarela",12,"Madeira")
print str(bol)
bol.trocarCor("Azul")
print "A cor foi alterada para ",bol.mostraCor()
print str(bol)  
#-------------------------------------------------------------------------------
print "-"*60+"\n2) Classe Quadrado: Crie uma classe que modele um quadrado:\n\
    Atributos: Tamanho do lado\n\
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área"+"-"*60
#-------------------------------------------------------------------------------
class Quadrado(object):
    def __init__(self,lado=0):
        self.lado=lado
    def mudarLado(self,novolado):
        self.lado=novolado
    def valorLado(self):
        return self.lado
    def calcArea(self):
        return self.lado*self.lado
    def __str__(self):
        return "(%sx%s) : %.3fcm²"%(self.lado,self.lado,self.calcArea())

q = Quadrado(3)
print str(q)
print "Aumentando o quadrado: "
q.mudarLado(9)
print "Ficou com lado: ",q.valorLado()
print "Sua área nova é: ",q.calcArea()
print "Veja:\n",str(q)
#-------------------------------------------------------------------------------
print "-"*60+"\n3) Classe Retangulo: Crie uma classe que modele um retangulo:\n\
    Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)\n\
    Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;\n\
    Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local. "+"-"*60
#-------------------------------------------------------------------------------
class Retangulo():
    def __init__(self,base=1,altura=1):
        self.__base=base
        self.__altura=altura
    @property
    def Altura(self):
        return self.__altura
    @Altura.setter
    def Altura(self,altura):
            assert float(altura)>0
            self.__altura=float(altura)
    @property
    def Base(self):
        return self.__base
    @Base.setter
    def Base(self,base):
            assert float(base)>0
            self.__base=float(base)
    def calcPerimetro(self):
        return self.__altura*2+self.__base*2
    def calcArea(self):
        return self.__altura*self.__base

while True:
    print "\n-- Calculo Retângulo --"
    ret=Retangulo()
    while True:
        try:
            base = int(raw_input("- Base.: "))
            ret.Base=base
            break
        except ValueError:
            print "- Base deve ser um número."
        except AssertionError:
            print "- O valor da base deve ser maior que zero."
    while True:
        try:
            altura = int(raw_input("- Altura.: "))
            ret.Altura=altura
            break
        except ValueError:
            print "- Altura deve ser um número."
        except AssertionError:
            print "- O valor da altura deve ser maior que zero."
    print "---- Relatório ----"
    print "Retângulo %fm por %fm "%(ret.Base,ret.Altura)
    print "Àrea: %fm²"%ret.calcArea()
    print "Perimetro: %fm"%ret.calcPerimetro()
    op = raw_input("- Deseja calcular outro retangulo? (s) ou (n): ")
    if op!="s": break
print "exit...\n"
#-------------------------------------------------------------------------------
print "-"*60+"\n4) Classe Pessoa: Crie uma classe que modele uma pessoa:\n\
    Atributos: nome, idade, peso e altura\n\
    Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm. "+"-"*60
#-------------------------------------------------------------------------------
class Pessoa():
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self,ano=1):
        self.idade += ano
    def engordar(self,kilos=1):
        self.peso += kilos
    def emagrecer(self, kilos=1):
        self.peso -= kilos
    def crescer(self, cm=0.5):
        self.altura += cm
    def __str__(self):
        return "%s, %d anos, %.2f kilos, %.2f cms."%(self.nome,self.idade,self.peso,self.altura)

pes = Pessoa('Lucas',21,80,177)
print str(pes)
pes.envelhecer()
print str(pes)
pes.engordar()
print str(pes)
pes.emagrecer(3)
print str(pes)
pes.crescer()
print str(pes)
#-------------------------------------------------------------------------------
print "-"*60+"\n5) Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios. . "+"-"*60
#-------------------------------------------------------------------------------
class ContaCorrente():
    def __init__(self,nConta,correntista,saldo=0):
        self.nConta = nConta
        self.correntista = correntista
        self.saldo=saldo
    def alterarNome(self,correntista):
        self.correntista = correntista
    def deposito(self,quantia):
        print "Deposito de R$%.2f..."%quantia
        self.saldo += quantia if quantia>0 else 0
    def saque(self,quantia):
        print "Saque de R$%.2f..."%quantia
        self.saldo -= quantia if quantia<=self.saldo else 0
    def __str__(self):
        return "Conta nº %d, Dono: %s, Saldo: %.2f"%(self.nConta,self.correntista,self.saldo)

cc=ContaCorrente(23,"Lucas")
print str(cc)
cc.deposito(500)
print str(cc)
cc.saque(120)
print str(cc)
#-------------------------------------------------------------------------------
print "-"*60+"\n6) Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas. "+"-"*60
#-------------------------------------------------------------------------------
class TV():
    def __init__(self,faixaIni=2,faixaFin=21,volIni=2,volFin=60):
        self.__fIni = faixaIni
        self.__fFin = faixaFin
        self.__vIni = volIni
        self.__vFin = volFin
        self.canalAtual = faixaIni
        self.volume = 0
    def setCanal(self,canal):
        assert canal>=self.__fIni and canal<=self.__fFin
        print "- Trocar canal para ",canal
        self.canalAtual = canal
    def setVolume(self,vol):
        assert vol>=self.__vIni and vol<=self.__vFin
        print "- Trocar volume para ",vol
        self.volume = vol
    def __str__(self):
        return "canal: %d, volume: %d"%(self.canalAtual,self.volume)

def TrocarCanal(tv):
    while True: 
        try:
            canal = int(raw_input("- Canal.: "))
            tv.setCanal(canal)
            break
        except ValueError:
            print "- Canal deve ser um número."
        except AssertionError:
            print "- O valor do canal inválido."

def TrocarVolume(tv):
    while True: 
        try:
            volume = int(raw_input("- Volume.: "))
            tv.setVolume(volume)
            break
        except ValueError:
            print "- Volume deve ser um número."
        except AssertionError:
            print "- O valor do volume inválido."

tv = TV(2,35)
while True:
    men={0:TrocarCanal,1:TrocarVolume}
    print "\n-- TV --"
    print str(tv)
    op = int(raw_input("Trocar Canal (0) ou Volume (1) ? :"))
    try:
        men[op](tv)
    except (KeyError,ValueError):
        print "Opção inválida!"
    print str(tv)
    op = raw_input("- Sair? (s) ou (n): ")
    if op=="s": break
print "exit...\n"
#-------------------------------------------------------------------------------
print "-"*60+"\n7) Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):\n\
    Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento. . "+"-"*60
#-------------------------------------------------------------------------------
class Tamagushi():
    def __init__(self,nome,fome=0,saude=0,idade=0):
        self._nome = nome
        self._fome = fome
        self._saude = saude
        self._idade = idade
    
    @property
    def Nome(self): return self._nome
    @Nome.setter
    def Nome(self,nome): self._nome = nome
    
    @property
    def Fome(self): return self._fome
    @Fome.setter
    def Fome(self,fome): self._fome = fome
    
    @property
    def Saude(self): return self._saude
    @Saude.setter
    def Saude(self,saude): self._saude = saude
    
    @property
    def Idade(self): return self._idade
    @Idade.setter
    def Idade(self,idade): self._idade = idade
    
    @property
    def Humor(self): return self._fome+self._saude 
#-------------------------------------------------------------------------------
print "-"*60+"\n8) Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?  "+"-"*60
#-------------------------------------------------------------------------------
class Macaco():
    def __init__(self,nome,bucho=[]):
        self._nome = nome
        self._bucho = bucho
    def comer(self, comida):
        self._bucho.append(comida)
    def verBucho(self):
        print "|- Conteúdo do estômago: "
        for comida in self._bucho:
            print "\t|- "+str(comida)
        if len(self._bucho)==0: print "\t|- vazio... :("
    def digerir(self):
        self._bucho = []
    def __str__(self):
        return self._nome

import time
mon = Macaco("Lipe")
print " - Macaco ",mon._nome
mon.verBucho()
print " - Irá comer... 'Arroz'"
mon.comer("Arroz")
mon.verBucho()
print " - Irá comer... 'Banana'"
mon.comer("Banana")
mon.verBucho()
print " - Irá comer... 'Banana' .. de novo"
mon.comer("Banana")
mon.verBucho()
print " - Ele está cheio...vamos deixar ele digerir..."
for i in range(3):
    time.sleep(1)
    print "..."
mon.digerir()
mon.verBucho()
print " - Irá comer... outro Macaco 0.0! "
mon.comer(Macaco("João"))
mon.verBucho()
#-------------------------------------------------------------------------------
print "-"*60+"\n9) Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:\n\
    Possua uma classe chamada Ponto, com os atributos x e y.\n\
    Possua uma classe chamada Retangulo, com os atributos largura e altura.\n\
    Possua uma função para imprimir os valores da classe Ponto\n\
    Possua uma função para encontrar o centro de um Retângulo.\n\
    Você deve criar alguns objetos da classe Retangulo.\n\
    Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.\n\
    A função para encontrar o centro do retângulo deve retornar o valor para\n\ um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.\n\
    O valor do centro do objeto deve ser mostrado na tela\n\
    Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo. "+"-"*60
#-------------------------------------------------------------------------------
class Ponto():
    def __init__(self,x=0,y=0):
        self.x=float(x)
        self.y=float(y)
    def __str__(self):
        return "(%.3f,%.3f)"%(self.x,self.y)

class Retangulo():
    def __init__(self,vertice,largura=1,altura=1):
        if not isinstance(vertice,Ponto): 
            raise TypeError,'Tipo %s não suportado.' % vertice.__class__.__name__ 
        self.__vertice=vertice
        self.__largura=largura
        self.__altura=altura
    @property
    def Altura(self):  
        return self.__altura
    @Altura.setter
    def setAltura(self,altura):
        if not isinstance(altura,float) or altura<=0: 
            raise ValueError, "Altura deve ser um número positivo."
        self.__altura = altura
    
    @property
    def Largura(self): 
        return self.__largura
    @Largura.setter
    def setLargura(self,largura):
        if not isinstance(largura,float) or largura<=0: 
            raise ValueError, "Largura deve ser um número positivo."
        self.__largura = largura
    
    @property
    def Vertice(self): 
        return self.__vertice
    @Vertice.setter
    def Vertice(self,vertice):
        if not isinstance(vertice,Ponto): 
            raise TypeError,'Tipo %s não suportado.'% verticePartida.__class__.__name__ 
        self.__vertice=vertice
    
    def showRec(self):
        return str(self.Largura)+"x"+str(self.Altura)
    def showDim(self):
        return "%.3fx%.3f"%(self.Largura, self.Altura)
    def centerPont(self):
        x = self.Largura/2
        x = self.Vertice.x+x if x>self.Vertice.x else self.Vertice.x-x
        y = self.Altura/2
        y = self.Vertice.y+y if y>self.Vertice.y else self.Vertice.y-y
        return Ponto(x,y)
    def printVertice(self):
        return str(self.Vertice) 
    def printCenterPont(self):
        return str(self.centerPont())

rec=Retangulo(Ponto())
def novo():
    global rec
    print "\n-- Criando um retângulo..."
    rec.Largura = float(raw_input("- Largura.: "))
    rec.Altura = float(raw_input("- Altura.: "))
    print "- Ponto de origem do retângulo %s:"%rec.showDim()
    x = float(raw_input("- X.: "))
    y = float(raw_input("- Y.: "))
    rec.Vertice = Ponto(x,y)
    
def Menu():
    global rec
    print "\n-- Criador de Retângulos --"
    while True:
        novo()
        print "\n- Retângulo Atual: ",rec.showRec()
        print "- Seu vertice: ",rec.printVertice()
        print "- Seu centro: ",rec.printCenterPont()
        op = raw_input("- Alterar dados do retangulo ? (s) ou (n) :")
        if op!="s": break
        
    print "...fim :("

print
Menu()
#-------------------------------------------------------------------------------
print "-"*60+"\n10) Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:\n\
    Possua uma classe chamada bombaCombustível, com no mínimo esses atributos: tipoCombustivel, valorLitro, quantidadeCombustivel \n\
    Possua no mínimo esses métodos:\n\
        abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo\n\
        abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.\n\
        alterarValor( ) – altera o valor do litro do combustível.\n\
        alterarCombustivel( ) – altera o tipo do combustível.\n\
        alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba. \n\
    OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.   "+"-"*60
#-------------------------------------------------------------------------------
class BombaCombustivel():
    def __init__(self,tipoCombustivel='g', valorLitro=0, quantidadeCombustivel=0):
        self._tipoCombustivel=tipoCombustivel
        self._valorLitro=valorLitro
        self._quantidadeCombustivel=quantidadeCombustivel
    def abastecerPorValor(self,valor):
        litros = valor/self._valorLitro
        if litros > self._quantidadeCombustivel: 
            raise ValueError, "\n- Quantidade de litros insuficiente para essa operação"
        print "\n |- Abastecimento por valor: R$%.2f - total: %.2f litros"%(valor,litros)
        self._quantidadeCombustivel-=litros
        return litros
    def abastecerPorLitro(self,litros):
        if litros > self._quantidadeCombustivel: 
            raise ValueError, "\n- Quantidade de litros insuficiente para essa operação"
        self._quantidadeCombustivel-=litros
        gasto = litros*self._valorLitro
        print "\n |- Abastecimento por litros: %.2f litros, foram gastos : R$%.2f"%(litros,gasto)
        return gasto
    def alterarValor(self,valor):
        self._valorLitro=valor
    def alterarCombustivel(self,tipo):
        self._tipoCombustivel=tipo
    def alterarQuantidadeCombustivel(self,quantia):
        print "\n |- Alterando a quantidade de combustivel para ",quantia
        self._quantidadeCombustivel=quantia
    def __str__(self):
        return "  - Tipo %s R$ %.2f por litro , total restante: %.4f"%(self._tipoCombustivel,  self._valorLitro, self._quantidadeCombustivel)


bc=BombaCombustivel('a',1.50,2000)
print str(bc)
bc.abastecerPorValor(500)
print str(bc)
bc.abastecerPorLitro(100)
print str(bc)
try:
    bc.abastecerPorValor(5000)
except ValueError,msg:
    print msg
bc.alterarQuantidadeCombustivel(4000)
print str(bc)
bc.abastecerPorValor(5000)
print str(bc)
#-------------------------------------------------------------------------------
print "-"*60+"\n11) Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:\n\
    Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.\n\
    O consumo é especificado no construtor e o nível de combustível inicial é 0.\n\
    Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.\n\
    Forneça um método obterGasolina( ), que retorna o nível atual de combustível.\n\
    Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:\n\
    meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. \n\
    meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. \n\
    meuFusca.andar(100);            # anda 100 quilômetros.\n\
    meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.  "+"-"*60
#-------------------------------------------------------------------------------
class Carro():
    def __init__(self,consumo,tanque=0):
        self._consumo=consumo
        self._qtdTanque=tanque
    def andar(self,distancia):
        assert distancia*self._consumo>self._qtdTanque , "- Seu veiculo não chega a essa distância, coloque mais combustivel !"
        self._qtdTanque -= distancia/self._consumo
    def obterGasolina(self): 
        return self._qtdTanque
    def adicionarGasolina(self,litros): 
        self._qtdTanque+= litros if litros>=0 else 0

meuFusca = Carro(15);              
meuFusca.adicionarGasolina(20);
print meuFusca.obterGasolina()  
try:
    meuFusca.andar(100);         
except AssertionError,mgs:
    print mgs             
meuFusca.adicionarGasolina(200);
print meuFusca.obterGasolina()  
meuFusca.andar(45); 
print meuFusca.obterGasolina()  
#-------------------------------------------------------------------------------
print "-"*60+"\n12) Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante."+"-"*60
#-------------------------------------------------------------------------------
class ContaCorrente():
    def __init__(self,nConta,correntista,saldo=0):
        self.nConta = nConta
        self.correntista = correntista
        self.saldo=saldo
    def alterarNome(self,correntista):
        self.correntista = correntista
    def deposito(self,quantia):
        self.saldo += quantia if quantia>0 else 0
    def saque(self,quantia):
        self.saldo -= quantia if quantia<=self.saldo else 0
    def __str__(self):
        return "%d dono: %s saldo: R$ %.2f"%(self.nConta,self.correntista,self.saldo)

class contaInvestimento(ContaCorrente):
    def __init__(self,nConta,correntista,taxaJuros,saldo=0):
        ContaCorrente.__init__(self,nConta,correntista,saldo)
        self.taxaJuros=taxaJuros
    def adicioneJuros(self):
        self.saldo += self.saldo*self.taxaJuros

cc = contaInvestimento(23,"Lucas",0.1,1000)
for i in range(5):
    print str(cc)
    cc.adicioneJuros()  
#-------------------------------------------------------------------------------
print "-"*60+"\n13) Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.   "+"-"*60
#-------------------------------------------------------------------------------
class Funcionario:
    def __init__(self,nome,salario):
        self.__nome=nome
        self.__salario=salario
    @property
    def Nome(self): 
        return self.__nome
    @Nome.setter
    def Nome(self,nome): 
        self.__nome=nome
    @property
    def Salario(self): 
        return self.__salario
    @Salario.setter
    def Salario(self,salario): 
        self.__salario=salario

f = Funcionario("Lucas","800")
print "-- Dados :"
print "- Nome: ",f.Nome
print "- Salario: ",f.Salario
f.Nome="Lucas Biason"
f.Salario=900
print "-- Novos Dados :"
print "- Nome: ",f.Nome
print "- Salario: ",f.Salario
#-------------------------------------------------------------------------------
print "-"*60+"\n14) Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.\n\
    Exemplo de uso:\n\
      harry=funcionário('Harry',25000)\n\
      harry.aumentarSalario(10)  "+"-"*60
#-------------------------------------------------------------------------------
class Funcionario:
    def __init__(self,nome,salario):
        self.__nome=nome
        self.__salario=salario
    @property
    def Nome(self): 
        return self.__nome
    @Nome.setter
    def Nome(self,nome): 
        self.__nome=nome
    @property
    def Salario(self): 
        return self.__salario
    @Salario.setter
    def Salario(self,salario): 
        self.__salario=salario
    def aumentarSalario(self,porcentual): 
        self.__salario = self.__salario+self.__salario*porcentual
        print "-- Recebeu um aumento de 10%..."
    def __str__(self):
        return "-- Dados :\n- Nome: %s\n- Salario: %.2f"%(self.__nome,self.__salario)

f = Funcionario("Lucas",800)
print str(f)
f.Nome="Lucas Biason"
f.Salario=900
print str(f)
f.aumentarSalario(0.1)
print str(f)
#-------------------------------------------------------------------------------
print "-"*60+"\n15) Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.   "+"-"*60
#-------------------------------------------------------------------------------
class Tamagushi():
    def __init__(self,nome,fome=0,saude=0,idade=0):
        self._nome = nome
        self._fome = fome
        self._saude = saude
        self._idade = idade
    
    @property
    def Nome(self): return self._nome
    @Nome.setter
    def Nome(self,nome): self._nome = nome
    
    @property
    def Fome(self): return self._fome
    @Fome.setter
    def Fome(self,fome): self._fome = fome
    
    @property
    def Saude(self): return self._saude
    @Saude.setter
    def Saude(self,saude): self._saude = saude
    
    @property
    def Idade(self): return self._idade
    @Idade.setter
    def Idade(self,idade): self._idade = idade
    
    @property
    def Humor(self): return self._fome+self._saude 
    
    def alimentar(self,comida): self._fome+=comida/10
    def brincar(self,tempo): self._saude+=tempo/10
#-------------------------------------------------------------------------------
print "-"*60+"\n16) Crie uma 'porta escondida' no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho.   "+"-"*60
#-------------------------------------------------------------------------------
class Tamagushi():
    def __init__(self,nome,fome=0,saude=0,idade=0):
        self._nome = nome
        self._fome = fome
        self._saude = saude
        self._idade = idade
    
    @property
    def Nome(self): return self._nome
    @Nome.setter
    def Nome(self,nome): self._nome = nome
    
    @property
    def Fome(self): return self._fome
    @Fome.setter
    def Fome(self,fome): self._fome = fome
    
    @property
    def Saude(self): return self._saude
    @Saude.setter
    def Saude(self,saude): self._saude = saude
    
    @property
    def Idade(self): return self._idade
    @Idade.setter
    def Idade(self,idade): self._idade = idade
    
    @property
    def Humor(self): return self._fome+self._saude 
    
    def alimentar(self,comida): self._fome+=comida/10
    def brincar(self,tempo): self._saude+=tempo/10
    def __str__(self):
        return "%s - Niveis:\nFome = %d\nSaúde =%d\nHumor =%d\n"%(self.Nome, self.Fome, self.Saude, self.Humor)

tama=Tamagushi("Flor")

def Alimentar():
    comida = int(raw_input("- Nivel de comida.:"))
    tama.alimentar(comida)
    print "Humor: ",tama.humor()

def Brincar():
    tempo = int(raw_input("- Tempo de brincadeira.:"))
    tama.brincar(tempo)
    print "Humor: ",tama.humor()

def Humor():
    print "Humor: ",tama.humor()

def Menu():
    menu={1:Alimentar,2:Brincar,3:Humor}
    while True:
        print "- Tamagushi -"
        print "1) Alimentar"
        print "2) brincar"
        print "3) Humor"
        print "0) Sair"
        op = int(raw_input("- Entre com a opção: "))
        if op==0: break
        if op==7: 
            print str(tama)
            continue
        menu[op]()

Menu()
#-------------------------------------------------------------------------------
print "-"*60+"\n17) Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.   "+"-"*60
#-------------------------------------------------------------------------------
class Tamagushi():
    def __init__(self,nome,fome=0,saude=0,idade=0):
        self._nome = nome
        self._fome = fome
        self._saude = saude
        self._idade = idade
    
    @property
    def Nome(self): return self._nome
    @Nome.setter
    def Nome(self,nome): self._nome = nome
    
    @property
    def Fome(self): return self._fome
    @Fome.setter
    def Fome(self,fome): self._fome = fome
    
    @property
    def Saude(self): return self._saude
    @Saude.setter
    def Saude(self,saude): self._saude = saude
    
    @property
    def Idade(self): return self._idade
    @Idade.setter
    def Idade(self,idade): self._idade = idade
    
    @property
    def Humor(self): return self._fome+self._saude 
    
    def alimentar(self,comida): self._fome+=comida/10
    def brincar(self,tempo): self._saude+=tempo/10
    def __str__(self):
        return "%s - Niveis:\nFome = %d\nSaúde =%d\nHumor =%d\n"%(self.Nome, self.Fome, self.Saude, self.Humor)

tamas=[]
def newTama():
    print "- Adicionando um novo amiguinhu a fazenda -"
    nome = raw_input("- Nome.: ")
    tamas.append(Tamagushi(nome))

def Alimentar():
    for tama in tamas:
        comida = int(raw_input("- %s - Nivel de comida.:"%tama.Nome))
        tama.alimentar(comida)
        print "- %s , humor: %s"%(tama.Nome,tama.Humor)

def Brincar():
    for tama in tamas:
        tempo = int(raw_input("- %s - Tempo de brincadeira.:"%tama.Nome))
        tama.brincar(tempo)
        print "- %s , humor: %s"%(tama.Nom,tama.Humor)

def Humor():
    for tama in tamas:
        print "- %s , humor: %s"%(tama.Nome,tama.Humor)

def init():
    tamas.append(Tamagushi("Flor",0,1,2))
    tamas.append(Tamagushi("José",3,0,1))
    tamas.append(Tamagushi("Lipe",1,2,0))

def secret():
    for tama in tamas: 
        print str(tama)

def Menu():
    init()
    menu={1:Alimentar,2:Brincar,3:Humor,4:newTama,7:secret}
    while True:
        try:
            print "- Tamagushi - Atualmente você tem %d tamaguchis "%len(tamas)
            print "1) Alimentar a todos"
            print "2) brincar com todos"
            print "3) Humor"
            print "4) Criar novo tama"
            print "0) Sair"
            op = int(raw_input("- Entre com a opção: "))
            if op==0: break
            menu[op]()
        except KeyError:
            print "- Opção inválida"


Menu()
