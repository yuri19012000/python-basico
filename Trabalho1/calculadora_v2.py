saida = ''  

def adicao(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b


def calculadora(num1, num2, operacao):
    operacao = operacao.lower() 

    if operacao == "+" or operacao == "adicao":
        resultado = adicao(num1, num2)

    elif operacao == "-" or operacao == "subtracao":
        resultado = subtracao(num1, num2)

    elif operacao == "*" or operacao == "multiplicacao":
        resultado = multiplicacao(num1, num2)

    elif operacao == "/" or operacao == "divisao":
        resultado = divisao(num1, num2)

    else:
        resultado = "Operação inválida"

    return resultado


while saida.lower() != 'n':
    print("\n=== Calculadora v2 ===")
    print("Operações possíveis: +, -, *, / ou adicao, subtracao, multiplicacao, divisao\n")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada: ")

    resultado = calculadora(num1, num2, operacao)

    print("Resultado da operação:", resultado)

    saida = input("Deseja continuar? (S/N): ")
