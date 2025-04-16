saldo = 0.0

while True:
    print("\n=== Menu da Conta Bancária ===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido! O depósito deve ser positivo.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        if valor <= 0:
            print("Valor inválido! O saque deve ser positivo.")
        elif valor > saldo:
            print("Saldo insuficiente para o saque.")
        else:
            saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    elif opcao == "3":
        print(f"Saldo atual: R${saldo:.2f}")

    elif opcao == "4":
        print("Saindo do sistema... Obrigado!")
        break

    else:
        print("Opção inválida! Escolha uma opção de 1 a 4.")