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
calorias06 = []
calorias07 = []
alimentoslista = {}

usuariogramas = {}
usuario_dias = {}
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
    if u[0] in usuario_dias:
        usuario_dias[u[0]].append(u[1])
    else:
         usuario_dias[u[0]] = [u[1]]
    nomes.append(u[1])
    #print(u)

del usuario_dias["Nome"]
del usuario_dias["Data"]
del usuario_dias["Fulano da Silva"]

del usuariogramas["Idade (anos)"]
del usuariogramas["Alimento"]
del usuariogramas["30"]



for i in usuario_dias["06/04/15"]: #calcula calorias para dia 06/04/15:
    if i in alimentos_calorias:
        q = float(alimentos_calorias[i])
        w = float(usuariogramas[i])
        x = (q*w)/100
        #print(x)
        calorias06.append(x)
        

for i in usuario_dias["07/04/15"]: #calcula calorias para dia 07/04/15:
    if i in alimentos_calorias:
        q = float(alimentos_calorias[i])
        w = float(usuariogramas[i])
        x = (q*w)/100
        #print(x)
        calorias07.append(x)


print(sum(calorias06))
print(sum(calorias07))