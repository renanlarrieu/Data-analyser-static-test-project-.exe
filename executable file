# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 22:24:04 2020

@author: Renan Larrieu
"""
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import scipy.interpolate
import numpy as np

x=[]
y=[]

t=0

print("Bem-vindo ao Graph Propulsion Maker")

nome_do_arquivo = str(input('Escreva o nome do arquivo que quer abrir com o seu respectivo formato .csv: '))

titulo_do_grafico = str(input('Escolha o título do seu gráfico: '))
    
titulo_do_eixo_x = str(input('Escolha o nome do eixo x do seu gráfico: '))

titulo_do_eixo_y = str(input('Escolha o nome do eixo y do seu gráfico: '))

nome_da_figura = str(input('Escolha o nome da figura que será salva :'))

#itulo_do_grafico = str('a')
    
#titulo_do_eixo_x = str('b')

#titulo_do_eixo_y = str('c')


g=float(9.8)


dados = open(nome_do_arquivo).readlines() #trocar para o nome_do_arquivo após testes de diagnóstico




def adiciona_dados():
    for i in range (len(dados)):
        if i !=0:  
            linha = dados[i].split(";")
            x.append(float(linha[0]))
            y.append(float(linha[1])*g)
            
            
        
adiciona_dados()
  


    
#def verifica_dados():   
 #   for i in y:
  #      
   #     
    #    if i < float(30):  
     ##      y.remove(i)
       #     x.remove(i)
            
        #else:  
         #   print('deu erro')
            
#verifica_dados()  
    
#print(x)
#print(y)    
    



    
fig1 = plt.gcf() #cria a figura    
plt.rcParams['figure.figsize'] = (20,12) #tamanho do gráfico
fig1, ax = plt.subplots() #anexa os subplots na figura
ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.rcParams['figure.figsize'] = (20,12) #tamanho do gráfico
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
#####y_interp = scipy.interpolate.interp1d(x, y)
#####print (y_interp(33.0))
fig1.savefig(nome_da_figura) #salva a figura em arquivo .png com qualidade em dpi

#-------------------------------------------------------------------------    
    
fmax = max(float(number) for number in y)


elemento = y.index(fmax)
t = (elemento) 


def integrate(x, y):
    area = np.trapz(y=y, x=x)
    return area



print('Os resultados de seu teste são:')
print('Impulso =',integrate(x, y),'N.s')
integrate(x,y)
#max(y, key=float)
print('Fmax =',fmax,'N')
print('Instante Fmáx =',x[t],'s')
print('Tempo de queima =',x[len(x)-1],'s')




fmax=str(fmax)
tempodequeima = x[len(x)-1]
tempodequeima = str(tempodequeima)


#--------------------------------------------------
resultados = "Os resultados de seu teste são:\n"

impulso = "Impulso = {}N.s\n"

força_max = "Fmax = {}N\n"

inst_fmax = "Instante Fmáx = {}s\n"

tempo_de_queima = "Tempo de queima = {}s\n"
#-------------------------------------------------------




arquivo = open("DADOS.txt","w")

arquivo.write(resultados)

arquivo.write(impulso.format(integrate(x,y)))

arquivo.write(força_max.format(fmax))

arquivo.write(inst_fmax.format(x[t]))

arquivo.write(tempo_de_queima.format(tempodequeima))

arquivo.close


os.system("PAUSE")
    
