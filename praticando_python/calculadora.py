import os

def calcular(indice, valor1, valor2):
    if indice == 0:
        return f"{valor1} + {valor2} = {valor1 + valor2}"
    elif indice == 1:
        return f"{valor1 - valor2}"
    elif indice == 2:
        return f"{valor1} * {valor2} = {valor1 * valor2}"
    elif indice == 3:
        try:
            return f"{valor1} / {valor2} = {valor1 / valor2}"
        except ZeroDivisionError:
            print(f"Divisão por {valor2} inválida")
    elif indice == 4:
        return f"{valor1} ** {valor2} = {valor1 ** valor2}"

def interface(operacoes):
    print(f"{'CALCULADORA':^23}")
    print("-"*23)
    for i in operacoes:
        print(f"| {i} | {operacoes[i]:<15} |")
    print("-"*23)
    print("\nEscolha a operação desejada:")

def main():
    operacoes = {
        0: "Soma",
        1: "Subtração",
        2: "Multiplicação",
        3: "Divisão",
        4: "Potência",
    }
    while True:
        interface(operacoes)
        
        while True:
            try:
                indice = int(input())
                operacoes[indice]
            except ValueError:
                os.system("cls")
                interface(operacoes)
                print("\033[1;31mPor favor digite apenas valores numéricos.\033[0;0m")
            except KeyError:
                os.system("cls")
                interface(operacoes)
                print("\033[1;31mOOPS, insira um opção válida.\033[0;0m")
            else:
                break

        print(f"\n>> Selecionada {operacoes[indice]}")

        valor1 = float(input("Primeiro valor: "))
        valor2 = float(input("Segundo valor: "))

        resultado = calcular(indice, valor1, valor2)
        if resultado:
            print(f"\nO resultado de {resultado}")
        while True:
            continuar = input("\nDeseja continuar? [Sim]/[Não]: ").lower()[0]
            if continuar not in 'sn':
                print("\033[1;31mInsira uma resposta válida.\033[0;0m")
            else:
                break
        
        if continuar == "n":
            break
        else:
            os.system("cls")
    print("Finalizando o programa")

if __name__ == "__main__":
    main()