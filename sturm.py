# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:56:17 2021

@author: thor2
"""
import numpy

def raicesenintervalo (funcion,derivada,inicio,final):
    n_funcion=len(funcion)
    n=len(derivada)
    lista=[]
    lista.append(funcion)
    lista.append(derivada)
    lista_1=[]
    lista_2=[]
    cambio_1=0
    cambio_2=0
    while n > 1 :
        n_1=len(lista)
        a=lista[n_1-2]
        b=lista[n_1-1]
        h,c=numpy.polydiv(a,b)
        lista.append(-c)
        n=len(c)
        #hasta aqui va bien
    for i in range(len(lista)):
        aux=0
        r=len(lista[i])
        for l in range(r):
            aux=aux*inicio+lista[i][l]
        lista_1.append(aux)
        aux=0
        for k in range(r):
            aux=aux*final+lista[i][k]
        lista_2.append(aux)
    print(lista_1)
    print(lista_2)
    #checkpoint, aún funciona
    for i in range(len(lista_1)-1):
        if lista_1[i]>0:
            if lista_1[i+1]>0:
                cambio_1+=0
            else:
                cambio_1+=1
        else:
            if lista_1[i+1]<0:
                cambio_1+=0
            else:
                cambio_1+=1
    for i in range(len(lista_2)-1):
        if lista_2[i]>0:
            if lista_2[i+1]>0:
                cambio_2+=0
            else:
                cambio_2+=1
        else:
            if lista_2[i+1]<0:
                cambio_2+=0
            else:
                cambio_2+=1
    
    print("Se encontraron ",cambio_1-cambio_2, " raíces en el intervalo ","[",inicio,",", final,"]")
raicesenintervalo([1,0,0,-4,0,1,-2],[6,0,0,-12,0,1],-2,2)