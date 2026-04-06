def boas_vindas(nome):
    print(f'Olá, {nome}! Seja bem-vindo!')

nome_digitado = input("Digite seu nome: ")
boas_vindas(nome_digitado)

def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado_soma = soma(num_a=5, num_b=3)
print(soma(num_a=17, num_b=8))

