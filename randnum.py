# from random import randint
#
# tentativa1 = 0
# numrand = randint(1, 10)
#
# while tentativa1 != numrand:
#     print(numrand)
#     tentativa = int(input('chute o número inteiro (1 a 10): '))
#
#
#     while type(tentativa) != int:
#         print('Digite apenas números inteiros!')
#
#     if tentativa == numrand:
#         tentativa1 = tentativa
#         print(f'Parabéns, você acertou, o número é: {numrand}')
#
#     elif tentativa > numrand:
#         print('O número que voce escolheu é maior que o número secreto, tente novamente!')
#
#     elif tentativa < numrand:
#         print('O número que você escolheu é menor que o número secreto, tente novamente!')

from random import randrange

"""
Objetivo: Criar um script que gerá um valor aleatoriamente, guarda este valor, e 
pergunta repetidamente para o usuário chutar o valor gerado até que ele acerte.
"""

valor_aleatorio = randrange(1, 11)


def is_integer(value):
    try:
        int(value)
        return True
    except:
        return False


while True:
    chute = input("Chute um número entre 1 e 10:\n")

    if not is_integer(chute):
        print("Informe um valor inteiro!\n")
        continue
    elif int(chute) == valor_aleatorio:
        print("Parabéns, você acertou!!!")
        break
    elif int(chute) > (valor_aleatorio + 2):
        print("Você chutou alto!")
        continue
    elif int(chute) < (valor_aleatorio - 2):
        print("Você chutou baixo!")
        continue
    else:
        print("Tá perto!!")
