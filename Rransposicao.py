"""
	* Projeto: Transposição
	* Autor: Joyce Claine e Marcos Monteiro 
	* Dados: 16/10/2020
	* Versao: 1.0
	* Data da ultima modificao: 16/10/2020
	* Descricao: Implementação da Cifra de Transposição. 
"""
import random

alfabeto  = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
             'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

print('********** CIFRA DE TRANSPOSIÇÃO **********\n')

#Mensagem que sera cifrada
chave = input("Digite a chave: ").upper()
frase = input("\nDigite a mensagem: ").upper()
print('\n')

lista_chave = [] #Lista paa armazenar a chave
lista_frase = [] #Lista para armazenar a frase

for i in range(len(frase)):
    if ord(frase[i])>90 or ord(frase[i])<65:
        continue
    lista_frase.append(frase[i])

for i in range(len(chave)):
    lista_chave.append(chave[i])

x = len(lista_chave)#Tamanho da lista que foi adicionada a chave
y = len(lista_frase)#Tamanho da lista que foi adicionada a frase

tamanho = (x * x) - x - y

while tamanho < 0:
    tamanho = tamanho + x

if tamanho > 0:
    for i in range(tamanho):
        lista_frase.append(random.choice(alfabeto))

contador = 0
temp = 0
M = [lista_chave]

#matriz preenchida com a chave e frase
while temp < len(lista_frase):
    l = []
    for j in range(len(lista_chave)):
        l.append(lista_frase[j + contador])
        temp+= 1
    contador+= len(lista_chave)
    M.append(l)

for i in range(len(M)):
    print(M[i])
 
minimo = 1000
index = 0
cifrar_texto = []

#cifrar mensagem. 
for j in range(x):
    for t in range(x):
        if M[0][t] == None:
            continue
        if ord(M[0][t]) < minimo:
            minimo = ord(M[0][t])
            index = t
    M[0][index] = None
    minimo = 1000
    for i in range(1,len(M)):
        cifrar_texto.append(M[i][index])

temp_2 = 1
tot = len(cifrar_texto)//len(lista_chave)

#imprimir mensagem crifrada 
print('\n------------------- MENSAGEM CIFRADA -------------------\n')
for n in range(len(cifrar_texto)):
    if temp_2 == tot:
        print(cifrar_texto[n], end = ' ')
        temp_2 = 1
    else:
        print(cifrar_texto[n], end = '')
        temp_2 += 1
print('\n')

#decifrar mensagem
print('\n------------------- DECIFRAR MENSAGEM -------------------\n')
chave = input("Digite a chave: ")
frase = input("Digite a frase cifrada: ")
print('\n')
lista_frase = [str(a) for a in frase.split(' ')]
lista_chave = []
n = []
v = []

for i in range(len(chave)):
    lista_chave.append(chave[i])
    v.append(chave[i])
    n.append(i)

for i in range(len(lista_chave)):
    lista_chave[i] = ord(lista_chave[i])

minimo = 1000
for i in range(len(lista_chave)):
    for j in range(len(lista_chave)):
        if lista_chave[j] == None:
            continue
        if lista_chave[j] < minimo:
            minimo = lista_chave[j]
            index = j
    v[index] = n[i]
    lista_chave[index] = None
    minimo = 1000

print(vetor)
#for i in range(len(v)):
#    print(lista_frase[v[i]])

