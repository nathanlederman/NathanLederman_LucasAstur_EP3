# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:15:18 2015

@author: Lucas
"""

usuario = open("usuario.csv", "r+").readlines()
#print (usuario)

alimentos = open("alimentos.csv", "r+").readlines()
#print(alimentos)
nomes = []

alimentoslista = {}

usuariogramas = {}

alimentos_calorias = {}
alimentos_proteinas = {}
alimentos_carboidratos = {}
alimentos_gorduras = {}



for i in alimentos:
    a = i.strip().split(",")
    #print (a)
    alimentos_calorias[a[0]] = a[2]
    alimentos_proteinas[a[0]] = a[3]
    alimentos_carboidratos[a[0]] = a[4]
    alimentos_gorduras[a[0]] = a[5]

del alimentos_calorias["Alimento"]
    
for i in usuario:
    u = i.strip().split(",")
    usuariogramas[u[1]] = u[2]
    nomes.append(u[1])
    print(u)
    
for i in range(len(usuario)):   
    if nomes[i] in alimentos_calorias:
        q = float(alimentos_calorias[nomes[i]])
        w = float(usuariogramas[nomes[i]])
        x = (q*w)/100
        print (x)                              


del usuariogramas["Idade (anos)"]
del usuariogramas["Alimento"]
del usuariogramas["30"]


print(alimentos_proteinas["CURRY"])