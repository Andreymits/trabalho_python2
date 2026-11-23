def mostrar_menu():
    print("\n--- CONTROLE FINANCEIRO ---")
    print("1 - Adicionar dinheiro")
    print("2 - Registrar gasto")
    print("3 - Ver saldo")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")
    return opcao


def adicionar_dinheiro(saldo):
    valor = float(input("Digite o valor que entrou: R$ "))
    saldo = saldo + valor
    print("Valor adicionado com sucesso!")
    return saldo


def registrar_gasto(saldo):
    valor = float(input("Digite o valor do gasto: R$ "))
    saldo = saldo - valor
    print("Gasto registrado com sucesso!")
    return saldo


def ver_saldo(saldo):
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    if saldo > 0:
        print("Seu saldo está positivo.")
    elif saldo < 0:
        print("Atenção: seu saldo está negativo!")
    else:
        print("Seu saldo está zerado.")


# Programa principal
saldo = 0.0
opcao = ""

while opcao != "4":
    opcao = mostrar_menu()

    if opcao == "1":
        saldo = adicionar_dinheiro(saldo)
    elif opcao == "2":
        saldo = registrar_gasto(saldo)
    elif opcao == "3":
        ver_saldo(saldo)
    elif opcao == "4":
        print("Encerrando o programa. Até mais!")
    else:
        print("Opção inválida! Tente novamente.")
