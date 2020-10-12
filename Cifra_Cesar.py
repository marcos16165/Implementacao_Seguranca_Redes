"""
	* Projeto: Cifra de César 
	* Autor: Joyce Claine e Marcos Monteiro 
	* Dados: 10/10/2020
	* Versao: 1.0
	* Data da ultima modificao: 10/10/2020
	* Descricao: Implementação da Cifra de César. 
"""


#Lista definindo os caracteres que sao aceitos
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B',
            'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W',
            'X', 'Y', 'Z']


print('********** CIFRA DE CÉSAR **********')
#Definindo quantidade de rotacoes
rotacoes = int(input("\nDigite a quantidade de rotações: "))

#Mensagem que sera cifrada 
frase = input("Digite a mensagem(Apenas letras): ")  

#n armazena o tamanho do alfabeto 52 
n = len(alfabeto)

cifrada = ""
decifrada = ""

#Percorrendo a frase de entrada
for i in frase:
    posicao = alfabeto.index(i) #Encontrando a posicao de cada palavra
    letra_cifrada = alfabeto[(posicao + rotacoes) %n] #Encontrando a nova posicao
    cifrada += letra_cifrada #Substituindo a posicao das letras

#Percorrendo a frase cifrada
for i in cifrada:
    posicao_cifrada = alfabeto.index(i) #Encontrando a posicao de cada palavra
    letra_decifrada = alfabeto[(posicao_cifrada - rotacoes) %n]
    decifrada += letra_decifrada #Decifrando mensagem 

while True:
    print("\n---------- MENU INÍCIO ----------")
    op = input("""
    1 - Mostrar mensagem cifrada
    2 - Mostrar mensagem original
    3 - Sair
    Digite sua opção: """)

    if op == '1':
        print("\n---------- MENSAGEM CIFRADA ----------\n")
        print(cifrada)

    elif op == '2':
        print("\n---------- MENSAGEM ORIGINAL ----------\n")
        #print(frase)
        print(decifrada)
        
    elif op == '3':
        print('\nSaindo do programa...')
        break
    else:
        print("\nEntrada invalida! Escolha uma opção.")

