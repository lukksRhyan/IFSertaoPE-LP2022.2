with open("texto.txt", 'w') as arqv:
    arqv.write("nigger")
    arqv.close()
#le um arquivo de texto, checa quais palavras sao palindromos e salvas ele em arquivos separadas
def ePalindromo(palavra = str()):

    letras = palavra.replace(' ', '')
    letras = letras.lower()
    inverso = letras[::-1]

    for char in range(len(letras)):
        if (letras[char] != inverso[char]):
            return False
    return True

with open('texto.txt', 'r') as texto:
    for linha in texto:
        print(linha)

with open('texto.txt', 'r') as texto:

    #with open('palindromes.txt', 'a') as palindromos:

        #for palavra in texto:
        #    print(ePalindromo(palavra))
            #    palindromos.write(palavra)

    print(ePalindromo('O bolo do lobo'))