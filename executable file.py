## atualização 

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 22:24:04 2020

@author: Renan Larrieu
"""
import time
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np
inicio = time.time()

xsemfiltro=[]#valores de tempo sem filtro

x=[]
y=[]

t=0

print("Bem-vindo ao Graph Propulsion Maker")



nome_do_arquivo = str(input('Escreva o nome do arquivo que quer abrir com o seu respectivo formato .csv, exemplo: "dadosdeteste.csv": '))

titulo_do_grafico = str(input('Escolha o título do seu gráfico: '))
    
titulo_do_eixo_x = str(input('Escolha o nome do eixo x do seu gráfico: '))

titulo_do_eixo_y = str(input('Escolha o nome do eixo y do seu gráfico: '))

nome_da_figura = str(input('Escolha o nome da figura que será salva :'))

nome_do_arquivo_de_texto = (input('Escolha o nome do arquivo de texto que será salvo contendo os cálculos presentes no código. Para isso, insira o nome do arquivo com seu respectivo formato .txt: '))


'''
titulo_do_grafico = str('a')
    
titulo_do_eixo_x = str('b')

titulo_do_eixo_y = str('c')

nome_da_figura = str('teste2')

nome_do_arquivo_de_texto = str('teste_texto.txt')

nome_do_arquivo = str('dados123.csv')
'''

g=float(9.8)


dados = open(nome_do_arquivo).readlines() #trocar para o nome_do_arquivo após testes de diagnóstico


filtro = float(6.1) #Este valor deve ser alterado dependendo da frequência de aquisição do transdutor HX711.
#frequência de aquisição é inversamente proporcional ao ruído.


def adiciona_dados():
    for i in range (0,len(dados),1):
        if float(dados[i].split(';')[1]) > float(filtro):
            xsemfiltro.append(round(float(dados[i].split(';')[0]),3))
            y.append(round(float(dados[i].split(';')[1])*g,3))
        else:
 
            None
            
           
def filtra_tempo():  
    for i in range(0,len(xsemfiltro),1):
        x.append(round(float((xsemfiltro[i]-xsemfiltro[0])/(1000)),3))
      

   
adiciona_dados()
filtra_tempo()

  
      
fig1 = plt.gcf() #cria a figura    
plt.rcParams['figure.figsize'] = (20,12) #tamanho do gráfico
fig1, ax = plt.subplots() #anexa os subplots na figura
ax.yaxis.set_minor_locator(tck.AutoMinorLocator())

fig1, ax = plt.subplots() #anexa os subplots na figura

#------------------------------------------------------
ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.title(titulo_do_grafico)#,' Força [N] x Tempo [S]') #título do grafico
plt.xlabel(titulo_do_eixo_x)
plt.ylabel(titulo_do_eixo_y)
#plt.xlabel('Tempo [s]') #nome do eixo x
#plt.ylabel('Força [N]') #nome do eixo y
plt.plot(x, y, color='black', linestyle = '-') #dois graficos em 1
plt.scatter(x, y, color='red', marker = '*')#, s= z) #dois graficos em 1
plt.fill_between(x,0,y, color = 'grey') #pinta a área sob a curva
plt.grid(True) #grade
plt.show() #plota
#plt.plot(x,y)

fig1.savefig(nome_da_figura) #salva a figura em arquivo .png com qualidade em dpi

#-------------------------------------------------------------------------    
    
fmax = max(float(number) for number in y)


elemento = y.index(fmax)
t = (elemento) 


def integrate(x, y):
    area = np.trapz(y=y, x=x)
    return area



print('Os resultados de seu teste são:')
print('Impulso =',round(integrate(x, y),3),'N.s')
integrate(x,y)
#max(y, key=float)
print('Fmax =',fmax,'N')
print('Instante Fmáx =',x[t],'s')
print('Tempo de queima =',x[len(x)-1],'s')




fmax=str(fmax)
tempodequeima = x[len(x)-1]
tempodequeima = str(tempodequeima)

fim = time.time()
tempo = round(fim - inicio,3)
print('Tempo de execução do programa =',tempo,'s')

#--------------------------------------------------
resultados = "Os resultados de seu teste são:\n"

impulso = "Impulso = {}N.s\n"

força_max = "Fmax = {}N\n"

inst_fmax = "Instante Fmáx = {}s\n"

tempo_de_queima = "Tempo de queima = {}s\n"

tempo_de_execução = "Tempo de execução do programa = {}s\n"
#-------------------------------------------------------




arquivo = open(nome_do_arquivo_de_texto,"w")

arquivo.write(resultados)

arquivo.write(impulso.format(round(integrate(x,y),3)))

arquivo.write(força_max.format(fmax))

arquivo.write(inst_fmax.format(x[t]))

arquivo.write(tempo_de_queima.format(tempodequeima))

arquivo.write(tempo_de_execução.format(tempo))

arquivo.close

#os.system("PAUSE")

    
