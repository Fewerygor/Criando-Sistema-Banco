menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
saques_n = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Digite o valor para saque: "))

        saldo_negativo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = saques_n > limite_saques

        if saldo_negativo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            saques_n += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ Extrato ================")

        if not extrato:
            print("Não houve movimentações realizadas!")
        else:
            extrato

        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
