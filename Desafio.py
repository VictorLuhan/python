opcoes = """
 [d] Depositar
 [s] Sacar
 [e] Extrato
 [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
nume_saque = 0
LIMITE_SAQUE =  3

while True:
    menu = input(opcoes)
    if menu == "d":
       valor = float(input("Digite o valor de deposito: "))

       if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
       else:
        print("Depósito não foi completado, tente novamente.")
    
    elif menu == "s":
       valor = float(input("Digite o valor que deseja sacar: "))
       
       excedeu_saldo = valor > saldo

       excedeu_limite = valor > limite

       excedeu_saque = nume_saque >= LIMITE_SAQUE

       if excedeu_saldo:
            print("O valor desejado excedeu o saldo em conta, tente novamente!")
       elif excedeu_limite:
            print("O valor ultrapassou o limite, tente novamente!")
       elif excedeu_saque:
            print("Limite de saque excedido")
       elif valor > 0:
          saldo -= valor
          extrato += f"Saque: R$ {valor:.2f}\n"
          nume_saque += 1
       else:
            print("Falha na operação! Valor informado é inválido.")
    elif menu == "e":
        print("\n ========EXTRATO========")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif menu == "q":
        break
    else:
        print("Operação inválida, digite uma opção válida.")    


