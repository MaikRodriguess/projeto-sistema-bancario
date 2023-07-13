menu = """

[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    #Deposito
    if opcao == "d":

        valor = float(input("Digite o valor para depósito: "))
            
        if valor > 0:
            saldo += valor
            extrato += f"\nDepósito: R$ {valor:.2f}"
        else:
             print("Valores negativos não são permitidos. Tente novamente")
         
        print(f"Depósito de :{valor:.2f}")

    # Saque   
    elif opcao == "s":
        valor = float(input("Digite o valor para saque: "))
        
        if numero_saques == LIMITE_SAQUES:
            print("O limite de saques diarios foi ultrapassado")
            continue
        elif valor > saldo:
            print("Não tem saldo suficiente na conta")
        elif valor > limite:
            print("Valor não permitido. Maior que limite diario")
        elif valor < 0:
            print("valor invalido para saque")

        numero_saques+=1
        saldo -= valor
        extrato += f"\nSaque: R$ {valor:.2f}"
        

    # Extrato    
    elif opcao == "e":
        
        print(f"""
        ========= Extrato =========: 
        {extrato}

        {f"Saldo: {saldo}"}
        ===========================
        """)
    # Sair
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")