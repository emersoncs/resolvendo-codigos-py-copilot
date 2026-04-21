# Testar se uma palavra é um palíndromo. Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

# Solicitando a palavra como entrada do usuário
palavra = input("Digite uma palavra: ")

#Como resultado, as palavras não estavam sendo consideradas iguais, mesmo quando eram palíndromos, por causa das letras maiúsculas e minúsculas. Para resolver isso, podemos converter a palavra para minúscula antes de fazer a comparação. Assim, "Ana" e "ana" serão consideradas iguais.
palavra = palavra.lower()

# Invertendo a palavra usando slicing
palavra_invertida = palavra[::-1]

# Verificando se a palavra é um palíndromo comparando a original com a invertida
if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:    print(f"A palavra '{palavra}' não é um palíndromo.")  
