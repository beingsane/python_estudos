#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#-------------------------------------------------------------------------------
# -- Lista Listas --
#-------------------------------------------------------------------------------
print "-"*60+"\n1) Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.\n"+"-"*60
#-------------------------------------------------------------------------------
lista=[]
for i in range(5):
    lista.append(int(raw_input(" Entre com um número inteiro: ")))
for i in range(5):
    print "lista[%d]=%d"%(i,lista[i])
#-------------------------------------------------------------------------------
print "-"*60+"\n2) Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.\n"+"-"*60
#-------------------------------------------------------------------------------
lista=[]
for i in range(10):
    lista.append(int(raw_input(" - Entre com um número: ")))
for i in range(-1,-len(lista)-1,-1):
    print "lista[%d]=%d"%(i,lista[i])
#-------------------------------------------------------------------------------
print "-"*60+"\n3) Faça um Programa que leia 4 notas, mostre as notas e a média na tela.\n"+"-"*60
#-------------------------------------------------------------------------------
notas=[]
media=0
for i in range(4):
    notas.append(float(raw_input(" - Entre o a "+str(i+1)+"ª nota: ")))
for i in range(len(notas)):
    media+=notas[i]
media/=len(notas)
print " - A média das notas é: %f"%(media)

#-------------------------------------------------------------------------------
print "-"*60+"\n4) Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.\n"+"-"*60
#-------------------------------------------------------------------------------
lista=[]
vogais='aeiou'
for i in range(10):
    lista.append(raw_input(" - Entre com um caracter: "))
print " - Consoantes:"
count=0
for c in lista:
    if c.lower() not in vogais:
        print " - ",c
        count+=1
print " - Foram ao todo %d consoantes. "%(count)
#-------------------------------------------------------------------------------
print "-"*60+"\n5) Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.\n"+"-"*60
#-------------------------------------------------------------------------------
vetor=[]
pares=[]
impares=[]
for i in range(20):
    n=int(raw_input(" - Entre com um número inteiro: "))
    vetor.append(n)
    if n%2==0:
        pares.append(n)
    else:
        impares.append(n)
print " ---- "
print " -  Você digitou: ",vetor
print " -  Pares: ",pares
print " -  Ímpares:",impares
print " ---- "
#-------------------------------------------------------------------------------
print "-"*60+"\n6) Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.\n"+"-"*60
#-------------------------------------------------------------------------------
medias=[]
for i in range(10):
    print "Entre com as notas do aluno (%d)"%(i+1) 
    media=0
    for y in range(4):
        n = float(raw_input(" - "+str(y+1)+"ª nota: "))
        media+=n
    media/=4
    medias.append(media)
print " - Alunos aprovados:"
for i in range(len(medias)):
    if medias[i]>=7 : print " - Aluno %d com média %f"%(i+1,medias[i])
#-------------------------------------------------------------------------------
print "-"*60+"\n7) Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.\n"+"-"*60
#-------------------------------------------------------------------------------
vetor=[]
soma, mul= 0, 1
for i in range(5):
    n = int(raw_input(" -Entre com um número: "))
    vetor.append(n)
    soma+=n
    mul*=n
print " ---- "
print " - Você entrou com: ",vetor
print " - Somas deles: ",soma
print " - Multiplicação deles: ",mul
print " ---- "
#-------------------------------------------------------------------------------
print "-"*60+"\n8) Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.\n"+"-"*60
#-------------------------------------------------------------------------------
alt, idad=[], []
for i in range(5):
    print " - Pessoa ",i
    alt.append(float(raw_input(" -Entre com a sua altura: ")))
    idad.append(int(raw_input(" -Entre com a sua Idade: ")))
print "\tAltura\tIdade"
for i in range(-1,-5,-1):
    print "\t%f\t%i"%(alt[i],idad[i])
#-------------------------------------------------------------------------------
print "-"*60+"\n9) Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.\n"+"-"*60
#-------------------------------------------------------------------------------
vetor=[]
for i in range(10):
    n = int(raw_input(" - Entre com um número: "))
    vetor.append(n)
som=0
for n in vetor:
    som+=(n*n)
print " - A soma dos quadrados dos elementos é ",som
#-------------------------------------------------------------------------------
print "-"*60+"\n10) Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.\n"+"-"*60
#-------------------------------------------------------------------------------
vetor1=[]
vetor2=[]
vetInter=[]
print " - Preenchendo o primeiro vetor: - "
for i in range(10):
    vetor1.append(int(raw_input(" -Entre com um número: ")))

print " - Preenchendo o segundo vetor: - "
for i in range(10):
    vetor2.append(int(raw_input(" -Entre com um número: ")))
    
for i,y in zip(vetor1,vetor2):
    vetInter.append(i)
    vetInter.append(y)

print " - Original 1:"
print "",vetor1
print " - Original 2:"
print "",vetor2
print " - Intercalado:"
print "",vetInter
#-------------------------------------------------------------------------------
print "-"*60+"\n11) Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.\n"+"-"*60
#-------------------------------------------------------------------------------
vetor1=[]
vetor2=[]
vetor3=[]
vetInter=[]
print " - Preenchendo o primeiro vetor: - "
for i in range(5):
    vetor1.append(int(raw_input(" -Entre com um número: ")))

print " - Preenchendo o segundo vetor: - "
for i in range(5):
    vetor2.append(int(raw_input(" -Entre com um número: ")))
print " - Preenchendo o terceiro vetor: - "
for i in range(5):
    vetor3.append(int(raw_input(" -Entre com um número: ")))

for z in range(5):
    vetInter.append(vetor1[z])
    vetInter.append(vetor2[z])
    vetInter.append(vetor3[z])

print " - Original 1:"
print "",vetor1
print " - Original 2:"
print "",vetor2
print " - Original 3:"
print "",vetor3
print " - Intercalado:"
print "",vetInter
#-------------------------------------------------------------------------------
print "-"*60+"\n12) Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.\n"+"-"*60
#-------------------------------------------------------------------------------
n = int(raw_input("- Entre com o número de alunos:"))
alunos=[]
avg=0
for i in range(n):
    print " -- Dados do Aluno nº",i," --"
    a=float(raw_input(" - Entre com a altura: "))
    i=int(raw_input(" - Entre com a idade: "))
    alunos.append((i,a))
    avg+=a
avg/=n
print " - Alunos com mais de 13 anos e acima da média de alturas:"
print "Aluno\tIdade\tAltura"
z=0
for i,a in alunos:
    if(a<avg or i<13): continue
    print "%d\t%d\t%f"%(z,a,i)
    z+=1
#-------------------------------------------------------------------------------
print "-"*60+"\n13) Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).\n"+"-"*60
#-------------------------------------------------------------------------------
temp=[]
mes={1:"Janeiro",2:"Fevereiro",3:"Março",4:"Abril",5:"Maio",6:"Junho",7:"Julho",8:"Agosto",9:"Setembro",10:"Outubro",11:"Novembro",12:"Dezembro"}

for i in range(12):
    temp.append(float(raw_input(" -Entre com a temperatura de "+mes[i+1]+":")))
    
avg=0
for i in range(len(temp)):
    avg+=temp[i]
avg/=len(temp)

print "-- Temperaturas acima da média deste ano: --"
print "Mês\t\tTemperatura"
for i in range(len(temp)):
    if temp[i]<avg: continue
    print "%s\t\t%f"%(mes[i+1],temp[i])
#-------------------------------------------------------------------------------
print "-"*60+"\n14) Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:'Telefonou para a vítima?' 'Esteve no local do crime?' 'Mora perto da vítima?' 'Devia para a vítima?' 'Já trabalhou com a vítima?' O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como 'Suspeita', entre 3 e 4 como 'Cúmplice' e 5 como 'Assassino'. Caso contrário, ele será classificado como 'Inocente'.n"+"-"*60
#-------------------------------------------------------------------------------
perg={}
perg[1]="Telefonou para a vitima?"
perg[2]="Esteve no local do crime?"
perg[3]="Mora perto da vitima?"
perg[4]="Devia para a vitima?"
perg[5]="Ja trabalhou com a vitima?"

qntAfirm=0
for v in perg.itervalues():
    stri=raw_input(str(v)+", (s) ou (n)?")
    if stri=='s': 
        qntAfirm+=1

print " - Resultado: %d questões."%(qntAfirm)
if qntAfirm<2:
    print "- Inocente"
elif qntAfirm<3:
    print "- Suspeita"
elif qntAfirm<5:
    print "- Cúmplice"
else:
    print "- Assassino" 
#-------------------------------------------------------------------------------
print "-"*60+"\n15) Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:\
Mostre a quantidade de valores que foram lidos;\
Exiba todos os valores na ordem em que foram informados,\ um ao lado do outro;\
Exiba todos os valores na ordem inversa à que foram\ informados, um abaixo do outro;\
Calcule e mostre a soma dos valores;\
Calcule e mostre a média dos valores;\
Calcule e mostre a quantidade de valores acima da média\ calculada;\
Calcule e mostre a quantidade de valores abaixo de sete;\
Encerre o programa com uma mensagem;\n"+"-"*60
#-------------------------------------------------------------------------------
valores=[]
i=0
while True:
    n = float(raw_input("- Entre com um valor ou -1 para sair:"))
    if n==-1:break
    valores.append(n)

print "-- Relátório: --"
print "- Mostre a quantidade de valores que foram lidos:",len(valores)
print "- Mostre todos os valores na ordem em que foram informados:",valores
print "- Mostre todos os valores na ordem inversa à que foram informados, um abaixo do outro"
for i in reversed(valores):
    print "- ",i
print "- Calcule e mostre a soma dos valores:"
som=0.0
for i in valores:
    som+=i
print " R: ",som
print "- Calcule e mostre a média dos valores:"
avg = som/len(valores)
print " R: ",avg
print "- Calcule e mostre a quantidade de valores acima da média calculada:"
qnt=0
for i in valores:
    if i>avg: qnt+=1
print " R: ",qnt
print "- Calcule e mostre a quantidade de valores abaixo de sete:"
qnt=0
for i in valores:
    if i<7: qnt+=1
print " R: ",qnt
print "-- fim --"
#-------------------------------------------------------------------------------
print "-"*60+"\n16) Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:\
$200 - $299 $300 - $399 $400 - $499 $500 - $599\
$600 - $699 $700 - $799 $800 - $899 $900 - $999\
$1000 em diante\n"+"-"*60
#-------------------------------------------------------------------------------
faixas={}
faixas[(200,299)]=0
faixas[(300,399)]=0
faixas[(400,499)]=0
faixas[(500,599)]=0
faixas[(600,699)]=0
faixas[(700,799)]=0
faixas[(800,899)]=0
faixas[(900,999)]=0
faixas[(1000,10000)]=0

vende=[]
while True:
    v = float(raw_input(" - Entre com o total de vendas do próximo vendedor ou -1 para sair "))
    if v==-1: break
    vende.append(200+(v*0.09))

for v in vende: 
    print "- Vendedor: R$",v
    for f,q in faixas.iteritems():
        if v>f[0] and v<f[1]: 
            faixas[f]=q+1
            print " |- Faixa Salárial: ",f
            break

print " -- Relatório Salárial --"
print "Faixa\t\t\tQnt de Vendedores"
for k,v in sorted(faixas.iteritems()):
    print "(%i,%i)\t\t\t%i"%(k[0],k[1],v)
#-------------------------------------------------------------------------------
print "-"*60+"\n17) Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:\n\
\n\
Atleta: Rodrigo Curvêllo\n\
\n\
Primeiro Salto: 6.5 m\n\
Segundo Salto: 6.1 m\n\
Terceiro Salto: 6.2 m\n\
Quarto Salto: 5.4 m\n\
Quinto Salto: 5.3 m\n\
\n\
Resultado final:\n\
Atleta: Rodrigo Curvêllo\n\
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3\n\
Média dos saltos: 5.9 m.\n"+"-"*60
#-------------------------------------------------------------------------------
saltos=[]
nome = raw_input("- Entre com o nome do atleta: ")
for i in range(5):
    saltos.append(float(raw_input("- Entre com a distancia do salto: ")))

print "Atleta: ",nome
print
print "Primeiro Salto: ",saltos[0],"m"
print "Segundo Salto:  ",saltos[1],"m"
print "Terceiro Salto: ",saltos[2],"m"
print "Quarto Salto:   ",saltos[3],"m"
print "Quinto Salto:   ",saltos[4],"m"
print
print "Resultado final:"
print "Atleta: ",nome
str1="Saltos: "
avg=0
for i in range(5):
     str1+=" "+str(saltos[i])+" -"
     avg+=saltos[i]
str1 = str1[:-1]
avg/=5
print str1
print "Média dos saltos: ",avg," m."
#-------------------------------------------------------------------------------
print "-"*60+"\n18) Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:\n\
O total de votos computados;\n\
Os númeos e respectivos votos de todos os jogadores que receberam votos;\n\
O percentual de votos de cada um destes jogadores;\n\
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.\n\
Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela. \n\
Enquete: Quem foi o melhor jogador?\n\
\n\
Número do jogador (0=fim): 9\n\
Número do jogador (0=fim): 10\n\
Número do jogador (0=fim): 9\n\
Número do jogador (0=fim): 10\n\
Número do jogador (0=fim): 11\n\
Número do jogador (0=fim): 10\n\
Número do jogador (0=fim): 50\n\
Informe um valor entre 1 e 23 ou 0 para sair!\n\
Número do jogador (0=fim): 9\n\
Número do jogador (0=fim): 9\n\
Número do jogador (0=fim): 0\n\
\n\
Resultado da votação:\n\
Foram computados 8 votos.\n\
Jogador Votos           %\n\
9               4               50,0%\n\
10              3               37,5%\n\
11              1               12,5%\n\
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.\n"+"-"*60
#-------------------------------------------------------------------------------
#- Inicia o dic de jogadores/pontuação
dic={}
for i in range(24):
    dic[i]=0
#- Inicia a votação
print "-- Enquete: --"
total=0
while True:
    n = int(raw_input("- Quem foi o melhor jogador? (1-23 ou 0 para sair):"))
    if n==0: break
    if n<0 or n>23: 
        print "- Númeração Inválida...Informe um valor entre 1 e 23..."
        continue
    total+=1
    dic[n]=dic[n]+1
#- Resultado da votação
print "--- Resultado da votação: ---"
print "- Foram computados ",total," votos."
if total!=0:
    print "Jogador\tVotos\t%"
    melhorId, melhor=0, dic[0]
    for i in range(24):
        print "",i,"\t",dic[i],"\t",(dic[i]*100/total),"%"
        if melhor<=dic[i]: 
            melhor, melhorId =dic[i], i
    print "O melhor jogador foi o número ",melhorId,", com ",melhor," votos, correspondendo a ",(melhor*100/total),"% do total de votos."
#-------------------------------------------------------------------------------
print "-"*60+"\n19) Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:\n'Qual o melhor Sistema Operacional para uso em servidores?'\nAs possíveis respostas são:\n\
1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n\
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:\n\
\n\
Sistema Operacional     Votos   %\n\
-------------------     -----   ---\n\
Windows Server           1500   17%\n\
Unix                     3500   40%\n\
Linux                    3000   34%\n\
Netware                   500    5%\n\
Mac OS                    150    2%\n\
Outro                     150    2%\n\
-------------------     -----\n\
Total                    8800\n\
O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.\n"+"-"*60
#-------------------------------------------------------------------------------
#- Inicia o dic de S.Os
dic={}
dic[0]=[0,"Windows"]
dic[1]=[0,"Unix"]
dic[2]=[0,"Linux"]
dic[3]=[0,"Netware"]
dic[4]=[0,"Mac OS"]
dic[5]=[0,"Outro"]
#- Inicia a votação
print "-- Enquete: --"
total=0
while True:
    n= int(raw_input("Qual o melhor Sistema Operacional para uso em servidores?\nAs possíveis respostas são:\n\n1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n0- Encerrar\n--?: "))
    if n==0: break
    if n<0 or n>6: 
        print "- Númeração Inválida...Informe um valor entre 1 e 6..."
        continue
    total+=1
    dic[n-1][0]+=1
print "--- Resultado da votação: ---"
print "- Foram computados ",total," votos."
if total!=0:
    print "Sistema Operacional\tVotos\t\t % "
    print "-------------------\t-----\t\t---"
    melhorId, melhor=0, dic[0][0]
    for i in range(6):
        print "",dic[i][1],"    \t\t",dic[i][0],"\t\t",(dic[i][0]*100/total),"%"
        if melhor<=dic[i][0]: melhor, melhorId = dic[i][0], i
    print "O Sistema Operacional mais votado foi o ",dic[melhorId][1],", com ",melhor," votos, correspondendo a ",(melhor*100/total),"% do total de votos."
#-------------------------------------------------------------------------------
print "-"*60+"\n20) As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.\n\nApós reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo: \n\
    a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:\n\
    O salário de cada funcionário, juntamente com o valor do abono;\n\
    O número total de funcionário processados;\n\
    O valor total a ser gasto com o pagamento do abono;\n\
    O número de funcionário que receberá o valor mínimo de 100 reais;\n\
    O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa. \n\
\n\
Projeção de Gastos com Abono\n\
============================ \n\
Salário: 1000\n\
Salário: 300\n\
Salário: 500\n\
Salário: 100\n\
Salário: 4500\n\
Salário: 0\n\
Salário    - Abono\n\
R$ 1000.00 - R$  200.00\n\
R$  300.00 - R$  100.00\n\
R$  500.00 - R$  100.00\n\
R$  100.00 - R$  100.00\n\
R$ 4500.00 - R$  900.00\n\
Foram processados 5 colaboradores\n\
Total gasto com abonos: R$ 1400.00\n\
Valor mínimo pago a 3 colaboradores\n\
Maior valor de abono pago: R$ 900.00\n"+"-"*60
#-------------------------------------------------------------------------------
abonos={}
total, totalAbono, maiorAbono, i =0, 0, 0, 0
while True:
    salarioBruto = float(raw_input("- Entre com o salário de Dezembro ou -1 para sair: "))
    if salarioBruto==-1: break
    abono = salarioBruto*0.2
    if abono<100: 
        abono=100
        total+=1
    if maiorAbono==0 or abono>maiorAbono: maiorAbono= abono 
    abonos[i]=salarioBruto+abono
    totalAbono+=abono
    i+=1

print
print "Projeção de Gastos com Abono"
print "============================ "
print "Func.\tSalario\n-----\t-------"
for i in abonos.iterkeys():
    print "",i,"\t",abonos[i],""
print
print "-- Foram processados ",i," colaboradores."
print "-- Total gasto com abonos: R$ ",totalAbono
print "-- Valor mínimo pago a ",total," colaboradores."
print "-- Maior valor de abono pago: R$ ",maiorAbono
print
#-------------------------------------------------------------------------------
print "-"*60+"\n21)Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:\n\
    O modelo do carro mais econômico;\n\
    Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. \n"+"-"*60
#-------------------------------------------------------------------------------
modelos={}
modMenor=0
for i in range(5):
    modelo =  raw_input("- Entre com um modelo de carro: ")
    consumo = float(raw_input("- Entre com o seu consumo: "))
    if modMenor==0 or consumo<modelos[modMenor]: 
        modMenor=modelo
    modelos[modelo]=consumo
print
print "-- Comparativo de Consumo de Combustível --"
print "==========================================="
i=0
for m in modelos.iterkeys():
    print "Veículo ",i,": ",m
    print "Km por litro:",modelos[m]
    print "------------------------------------------"
    i+=1
i=0
print
print "-- Relatório Final --"
print "---------------------"
for m in modelos.iterkeys():
    print i,"- ",m," - ",modelos[m]," - ",float(1000/modelos[m])," litros - R$ ",float(1000/modelos[m])*2.25
    print "Km por litro:",modelos[m]
    print "------------------------------------------"
    i+=1
print "O menor consumo é do ",modMenor,"."
#-------------------------------------------------------------------------------
print "-"*60+"\n22)Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.\n\
    Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:\n\
    necessita da esfera;\n\
    necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. \n"+"-"*60
#-------------------------------------------------------------------------------
defeitos={1:[0,"necessita da esfera"],2:[0,"necessita de limpeza"],3:[0,"necessita troca do cabo"],4:[0,"quebrado ou inutilizado"]}
str1="- Entre com o código do defeito: \n"
for i,s in defeitos.items():
    str1+= str(i)+' - '+str(s[-1])+'\n' 
str1+=" - ou -1 para sair:"   
total=0
while True:
    defeito = int(raw_input(str1))
    if defeito==-1: break
    if defeito not in defeitos:
        print "- Defeito inválido..."
        continue
    defeitos[defeito][0]=defeitos[defeito][0]+1
    total+=1
print
print "============================="
print " ---      Relatório      --- "
print "============================="
print "Quantidade de mouses:",total
print "Situação\t\tQuantidade\tPercentual"
for i in defeitos.iterkeys():
    print defeitos[i][1],'\t\t',defeitos[i][0],"\t",defeitos[i][0]*100/total,"%"
#-------------------------------------------------------------------------------
print "-"*60+"\n23) A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado 'usuarios.txt': \n\
alexandre       456123789\n\
anderson        1245698456\n\
antonio         123456456\n\
carlos          91257581\n\
cesar           987458\n\
rosemary        789456125\n\
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado 'relatório.txt', no seguinte formato: \n\
ACME Inc.               Uso do espaço em disco pelos usuários\n\
------------------------------------------------------------------------\n\
Nr.  Usuário        Espaço utilizado     % do uso\n\
1    alexandre       434,99 MB             16,85%\n\
2    anderson       1187,99 MB             46,02%\n\
3    antonio         117,73 MB              4,56%\n\
4    carlos           87,03 MB              3,37%\n\
5    cesar             0,94 MB              0,04%\n\
6    rosemary        752,88 MB             29,16%\n\
Espaço total ocupado: 2581,57 MB\n\
Espaço médio ocupado: 430,26 MB\n\
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.\n"+"-"*60
#-------------------------------------------------------------------------------
dic={}
#Conversão para MB
def toMB(bytes):
    return float(bytes/1024)
#Calculo Porcentagem
def perCent(bytes,total):
    return float(toMB(bytes)*100/toMB(total))
#Calculo media
def calAVG(bytes,totalF):
    return float(toMB(bytes)/totalF)
#Trazendo arquivo
filename= "usuarios.txt"
f = open(filename,'r')
allLines=f.readlines()
f.close()
#montando dicionario de dados
totalSpace, totalF = 0, 0
for eachLine in allLines:
    nome = eachLine[:16]
    use=int(eachLine[16:])
    dic[nome]=use
    totalSpace+=use
    totalF+=1
#geração do relatório
print "ACME Inc.               Uso do espaço em disco pelos usuários"
print "-----------------------------------------------------------------------"
print "Nr.  Usuário\t\tEspaço utilizado\t% do uso"
i=0
for k,v in dic.items():
    print i,"  ",k,"\t",toMB(v)," MB\t\t"+str(perCent(v,totalSpace))+"%"
print "Espaço total ocupado: ",toMB(totalSpace)," MB"
print "Espaço médio ocupado: ",calAVG(totalSpace,totalF)," MB"
#-------------------------------------------------------------------------------
print "-"*60+"\n24) Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados. \n"+"-"*60
#-------------------------------------------------------------------------------
import random
def lancar():
    faces=[0,1,2,3,4,5,6]
    random.shuffle(faces)
    return faces[0]

listFaces= {}.fromkeys(range(7),0)
print listFaces
for i in range(1000000):
    f = lancar()
    listFaces[f]=listFaces[f]+1

for k,v in listFaces.items():
    print "Face: ",k," - ",v," vezes.", (v*100/1000000),"%"


