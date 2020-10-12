"""
	* Projeto: Cifra Monoalfabetica 
	* Autor: Joyce Claine e Marcos Monteiro 
	* Dados: 12/10/2020
	* Versao: 1.0
	* Data da ultima modificao: 12/10/2020
	* Descricao: Implementação da Cifra Monoalfabetica. 
"""

#Plain: abcdefghijklmnopqrstuvwxyz

#Cipher: DKVQFIBJWPESCXHTMYAUOLRGZN

alfabeto1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z',
             'D', 'K', 'V', 'Q', 'F', 'I', 'B',
             'J', 'W','P', 'E', 'S', 'C', 'X',
             'H', 'T','M', 'Y', 'A', 'U', 'O',
             'L', 'R','G', 'Z', 'N']


print('********** CIFRA MONOALFABÉTICA **********')

#Mensagem que sera cifrada 
frase = input("\nDigite a mensagem(Apenas letras): ")  

#x armazena o tamanho do alfabeto 52 
x = len(alfabeto1)

cifrada = ""
decifrada = ""

#Cifrando
for i in frase:
    posicao = alfabeto1.index(i) #Encontrando a posicao de cada palavra
    letra_cifrada = alfabeto1[(posicao + 26)%x] #Encontrando a nova posicao
    cifrada += letra_cifrada

#Decifrando
for i in cifrada:
    posicao = alfabeto1.index(i) #Encontrando a posicao de cada palavra
    letra_decifrada = alfabeto1[(posicao - 26)%x] #Encontrando a nova posicao
    decifrada += letra_decifrada
   
    
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


    
