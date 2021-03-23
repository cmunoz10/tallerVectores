# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:37:11 2021

@author: camun
"""

#punto 1

import numpy as np
numeros=[]
cantidadElementos=int(input('digite la cantidad de elementos :'))
for i  in range (0, cantidadElementos):
    numero=float(input(f'Digite el numero{i+1} : '))
    numeros.append(numero)
sumatoria=sum(numeros)
productoria=np.prod(numeros)
menorElemento=min(numeros)
mayorElemento=max(numeros)
print(f'la sumatoria de los {cantidadElementos} elementos es : {sumatoria}')
print(f'la productoria de los {cantidadElementos} elementos es : {productoria}')
print(f'El menor elemento de la lista es el : {menorElemento}')
print(f'El mayor elemento de la lista es el : {mayorElemento}')

#punto 2

numeros=[]
cantidadPares=0
cantidadImp=0
cantidadPrimos=0
divisores=0
cantidadElementos=int(input('digite la cantidad de elementos :'))
for i  in range (1, cantidadElementos+1):
    numero=float(input(f'Digite el numero {i} : '))
    numeros.append(numero)
    divisores=0
   
    for j  in range (1, cantidadElementos+1):
        if numero%j == 0:
            divisores=divisores+1
     
    if numero%2 == 0 :
        cantidadPares=cantidadPares+1
    elif numero%2 != 0 :
        cantidadImp=cantidadImp+1
    elif divisores<2:
        cantidadPrimos=cantidadPrimos+1
        
print(f'La cantidad de numeros pares es : {cantidadPares}')
print(f'La cantidad de numeros impares es : {cantidadImp}')
print(f'La cantidad de numeros primos es : {cantidadPrimos}')


#punto 3

v1=[]
s=[]
r=[]
v=[]
cantidadElementos=int(input('digite la cantidad de elementos de los vectores:'))

for i  in range (1, cantidadElementos+1):
    numerov=float(input(f'Digite el numero {i} del vector v : '))
    v.append(numerov)
    numero=float(input(f'Digite el numero {i} del vector v1: '))
    v1.append(numerov)
    suma=numerov+numero
    resta=numerov-numero
    s.append(suma)
    r.append(resta)
print(f'vector de la suma es  : {s}')
print(f'vector de la resta es  : {r}')

#punto 4

from scipy import stats
import numpy as np 
repetido=0
v=[]
cantidadElementos=float(input('digite la cantidad de elementos del vector:'))

for i  in range (1, cantidadElementos+1):
    numerov=float(input(f'Digite el numero {i} del vector v : '))
    v.append(numerov)
print(v)
moda, count = stats.mode(np.array(v))

print(f'el numero que mas re sepite es {moda}')

#punto 5

import numpy as np 
v=[]
s=[]
p=[]

cantidadElementos=int(input('digite la cantidad de elementos del vector:'))
mitad=cantidadElementos/2
if cantidadElementos%2!=0:
    mitad2=mitad+1
else:
    mitad2=mitad
for i  in range (1, cantidadElementos+1):
    numero=int(input(f'Digite el numero {i} del vector v: '))
    v.append(numero)
    if i<=mitad:
        s.append(numero)
    elif i>mitad2:
        p.append(numero)
sumatoria=sum(s)
productoria=np.prod(p)
print(v)
print(f'la sumatoria es : {sumatoria}')
print(f'la productoria es : {productoria}')

#punto 6
v=[]
s=[]
p=[]
simetrico=0

cantidadElementos=int(input('digite la cantidad de elementos del vector:'))
mitad=int(cantidadElementos/2)
dato=mitad
if cantidadElementos%2!=0:
    mitad2=mitad+1
else:
    mitad2=mitad
for i  in range (1, cantidadElementos+1):
    numero=float(input(f'Digite el numero {i} del vector v: '))
    v.append(numero)
    if i<=mitad:
        s.append(numero)
    elif i>mitad2:
        p.append(numero)
print(s)
print(p)
for i in range(0, mitad):
    print(dato)
    print("----")
    print(p[dato-1])
    if s[i]!=p[dato-1]:
        simetrico=1
    dato=dato-1
    
if simetrico==1:
    print("no simetrico")
else:
    print("es simetrico")

#punto 7

        
a=[]
b=[]
cantidadElementos=int(input('digite la cantidad de elementos del vector:'))
for i  in range (1, cantidadElementos+1):
    numeroa=float(input(f'Digite el numero {i} del vector A : '))
    a.append(numeroa)
for i  in range (1, cantidadElementos+1):
    numerob=float(input(f'Digite el numero {i} del vector B : '))
    b.append(numerob)
A=set(a)
B=set(b)
union= A | B 
diferenciaA = A - B
diferenciaB = B - A
interseccion=A & B
print(f'la union de los dos vectores es {union}')
print(f'la diferencia de A - B es : {diferenciaA}')
print(f'la diferencia de B - A es : {diferenciaB}')
print(f'la interseccion de ambos es : {interseccion}')



   







