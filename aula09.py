frase = 'Curso em Video Python'
print(frase[3])  # Imprime o caractere na posição 3
print(frase[3:13])  # Imprime os caracteres da posição 3 até a 12
print(frase[:13])  # Imprime os caracteres do início até a posição 12
print(frase[13:])  # Imprime os caracteres da posição 13 até o final
print(frase[1:15:2])  # Imprime os caracteres da posição 1 até a 14, pulando de 2 em 2
print(frase[::2])  # Imprime todos os caracteres, pulando de 2 em 2
print(frase.count('o'))  # Conta quantas vezes o caractere 'o' aparece
print(frase.upper().count('O'))  # Conta quantas vezes 'O' aparece em maiúsculo
print(len(frase))  # Imprime o tamanho da string
print(len(frase.strip()))  # Imprime o tamanho da string sem espaços no início e no final
print(frase.lower().find('video'))  # Encontra a posição da substring 'video' em minúsculo
print(frase.split())  # Divide a string em uma lista de palavras

print(frase.replace('Python', 'Android'))  # Substitui 'Python' por 'Android'
print(frase)

frase = frase.replace('Python', 'Android')
print(frase)

print('Oi')
print ('''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum 
       has been the industrys standard dummy text ever since the 1500s''')

