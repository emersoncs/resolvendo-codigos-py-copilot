# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!
dado1 = input("Digite o primeiro dado: ")
dado2 = input("Digite o segundo dado: ")

# Concatenando
resultado = dado1 + " " + dado2
print("Resultado da concatenação:", resultado)

# Podemos também usar a função format para concatenar os dados
resultado_format = "{} {}".format(dado1, dado2)
print("Resultado da concatenação usando format:", resultado_format)
