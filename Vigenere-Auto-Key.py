"""
	* Projeto: Cifra de Vigenère 
	* Autor: Joyce Claine e Marcos Monteiro 
	* Dados: 12/10/2020
	* Versao: 1.0
	* Data da ultima modificao: 12/10/2020
	* Descricao: Implementação da Cifra Vigenère. 
"""


# Listas com o alfabeto
lista01 = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
         'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
         'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
         'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
         'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

lista02 = {0:'a',1:'b',2:'c',3:'d',4:'e',
       5:'f',6:'g',7:'h',8:'i',9:'j',
       10:'k',11:'l',12:'m',13:'n',14:'o',
       15:'p',16:'q',17:'r',18:'s',19:'t',
       20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}

#-----------------------------------------------------------------
#Gerando chave de forma que ela se repita até ficar do tamanho do texto original
def gerar_chave(mensagem,chave):
	x = len(mensagem) #Determinando tamanho da mensagem de entrada
	i = 0 # contador
	#Bloco para modificar o tamanho da chave
	while True:
		if x == i:
			i = 0
		if len(chave)== len(mensagem):
			break #Para caso o tamanho da chave seja igual ao da mensagem
		chave += chave[i]
		i +=1 
	return chave
    
#-----------------------------------------------------------------
#Criptografando o texto de entrada
def cifrarTexto(mensagem,nova_chave):
	cifrar_texto = ''
	i = 0
	for letra in mensagem: #Percorrendo a mensagem de entrada
		if letra == ' ': 
			cifrar_texto += ' '
		else:
                        #X vai receber a posição de cada letra + o indice da chave
			x = (lista01[letra] + lista01[nova_chave[i]]) % 26
			i += 1
			cifrar_texto += lista02[x]
	return cifrar_texto
   
#-----------------------------------------------------------------
#Descriptografando o texto
def textoOriginal(cifrar_texto,nova_chave):
	or_txt = ''
	i = 0
	#Processo inverso a cifragem, devolve a palavra original
	for letra in cifrar_texto:
		if letra == ' ':
			or_txt += ' '
		else:
			x =(lista01[letra]-lista01[nova_chave[i]]+26)%26
			i += 1
			or_txt += lista02[x]
	return or_txt

#-----------------------------------------------------------------
    
#def main():
print('****************** CIFRA DE VIGENERE ******************')
entrada = input("\nDigite a mensagem(letras minúsculas): ")
chave = input("Digite a chave: ")

nova_chave = gerar_chave(entrada,chave)
cifrar_texto = cifrarTexto(entrada,nova_chave)
original_texto = textoOriginal(cifrar_texto,nova_chave)
	
print("Chave = " + nova_chave)
print("Texto Original = " + original_texto)
print("Texto Cifrado = " + cifrar_texto.upper())

