# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:15:18 2015

@author: Lucas
"""

usuario = open("usuario.csv", "r+").readlines()
print (usuario)

alimentos = open("alimentos.csv", "r+").readlines()
print(alimentos)

alimentoslista = {}

usuariogramas = {}

for i in alimentos:
    a = i.strip().split(",")
    print (a)
    
    
    
for i in usuario:
    u = i.strip().split(",")
    usuariogramas[u[1]] = u[2]


del usuariogramas["Idade (anos)"]
del usuariogramas["Alimento"]
del usuariogramas["30"]


print(usuariolista)