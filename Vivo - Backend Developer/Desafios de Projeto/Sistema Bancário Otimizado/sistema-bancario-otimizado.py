import datetime

def mostrar_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    """
    return input(menu)

def depositar(saldo):
    v_deposito = int(input("Valor para depósito: \n"))
    if v_deposito < 1:
        print("Atenção, insira um valor válido!")
    else:
        saldo += v_deposito
        print(f"Saldo atual: R$ {saldo:.2f}")
    return saldo

def sacar(saldo, numero_saque, LIMITE_SAQUE, limite, extrato):
    if numero_saque >= LIMITE_SAQUE:
        print("Limite de saque diário atingido!")
    else:
        v_saque = int(input("Valor que deseja sacar: \n"))
        if v_saque > saldo:
            print("Atenção, saldo insuficiente!")
        elif v_saque > limite:
            print("Atenção, limite de saque (R$ 500,00) excedido!")
        else:
            saldo -= v_saque
            numero_saque += 1
            extrato += f"Saque: R$ {v_saque:.2f}\n"
            print(f"Saldo atual: R$ {saldo:.2f}")
    return saldo, numero_saque, extrato

def mostrar_extrato(saldo, extrato):
    print("\n------------------------ EXTRATO ------------------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}\nData: {datetime.datetime.now()}")
    print("---------------------------------------------------------")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    LIMITE_SAQUE = 3

    while True:
        opcao = mostrar_menu()

        if opcao == "d":
            saldo = depositar(saldo)
        elif opcao == "s":
            saldo, numero_saque, extrato = sacar(saldo, numero_saque, LIMITE_SAQUE, limite, extrato)
        elif opcao == "e":
            mostrar_extrato(saldo, extrato)
        elif opcao == "q":
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
