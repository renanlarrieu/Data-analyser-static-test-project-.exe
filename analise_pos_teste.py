# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 22:24:04 2020

@author: Renan Larrieu
"""
#import os
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import pandas as pd
import numpy as np

g=float(9.8)

print("Bem-vindo ao Graph Propulsion Maker")

nome_do_arquivo = str(input('Escreva o nome do arquivo que quer abrir com o seu respectivo formato .csv, exemplo: "dadosdeteste.csv": '))

#exemplo-> nome_do_arquivo = 'teste.csv'

data = pd.read_csv(nome_do_arquivo, sep=',') #extrai os dados do arquivo .csv e armazena na variável 'data' em forma de panda

x_pd = data['Tempo']
y_pd = data['Massa']

y = y_pd.tolist()
x = x_pd.tolist()

for i in range (0,len(x)):
    x[i]=float(x[i])
    y[i]=float(y[i])
       
for i in range(0,len(y)):
    y[i]=y[i]*g
 
x_inicial=x[0]

for i in range (0,len(x)):
    x[i]=(x[i]-x_inicial)*0.001 

t=0

titulo_do_grafico = str(input('Escolha o título do seu gráfico: '))

nome_da_figura = str(input('Escolha o nome da figura que será salva :'))

nome_do_arquivo_de_texto = (input('Escolha o nome do arquivo de texto que será salvo contendo os cálculos presentes no código. Para isso, insira o nome do arquivo com seu respectivo formato .txt: '))
  
fig1 = plt.gcf() #cria a figura    
fig1, ax = plt.subplots() #anexa os subplots na figura
ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.rcParams['figure.figsize'] = (60,30) #tamanho do gráfico
plt.rcParams.update({'font.size': 22}) #configura o tamanho da fonte dos parametros


#--------------------------------------------------------------------------

ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.title(titulo_do_grafico,fontsize=35)#,' Força [N] x Tempo [S]') #título do grafico
plt.xlabel('Tempo [s]',fontsize=30) #nome do eixo x
plt.ylabel('Força [N]',fontsize=30) #nome do eixo y
plt.plot(x, y, color='black', linestyle = '-') #dois graficos em 1
plt.scatter(x, y, color='red', marker = '*')  #dois graficos em 1
plt.fill_between(x,0,y, color = 'grey') #pinta a área sob a curva
plt.grid(True,which='both') #grade
plt.tick_params(labelsize=30);
plt.show() #plota
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
impulso = str(round(integrate(x,y),3))
print('Fmax =',round(fmax,3),'N')
print('Instante Fmáx =',x[t],'s')
print('Tempo de queima =',x[len(x)-1],'s')

fmax=str(round(fmax,3))

tempodequeima = x[len(x)-1]
tempodequeima = str(round(tempodequeima,3))

#--------------------------------------------------
resultados = "Os resultados de seu teste são:\n"

impulso_str = "Impulso = {}N.s\n"

forca_max = "Fmax = {}N\n"

inst_fmax = "Instante Fmáx = {}s\n"

tempo_de_queima = "Tempo de queima = {}s\n"
#----------------------------------------------------

arquivo = open(nome_do_arquivo_de_texto,"w")

arquivo.write(resultados)

arquivo.write(impulso_str.format(impulso))

arquivo.write(forca_max.format(fmax))

arquivo.write(inst_fmax.format(x[t]))

arquivo.write(tempo_de_queima.format(tempodequeima))

arquivo.close

#os.system("PAUSE")
    