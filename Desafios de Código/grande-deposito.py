valor = float(input())

if valor > 0:
    saldo_formatado = "{:.2f}".format(valor).replace(',', '.')
    print("Deposito realizado com sucesso!\nSaldo atual: R$", saldo_formatado)
    
elif valor == 0:
    print("Encerrando o programa...")
   
else:
    print("Valor invalido! Digite um valor maior que zero.")