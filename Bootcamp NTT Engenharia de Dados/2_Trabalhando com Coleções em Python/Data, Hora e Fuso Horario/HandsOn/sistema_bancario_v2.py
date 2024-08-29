from datetime import datetime

# menu de operações
menu = """
Digite a opção desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Inicialização de variáveis
saldo = 0;
limite = 500;
extrato = "";
numero_saques = 0;
LIMITE_SAQUES = 3;
LIMITE_OPERACOES = 10;
operacoes = 0;
now = datetime.now();


while True:

    opcao = input(menu);

    if opcao == "d":
        if operacoes < LIMITE_OPERACOES:
            concluido = False;
        
        else:
            print("Número de operações diárias excedido.");
            concluido = True;
        
        # roda até um valor válido ser informado
        while not concluido :
            valor = float(input("\nInforme o valor do depósito ou digite '0' para voltar: "));

            if valor == 0:
                break;
            
            # testa para valor positivo
            elif valor > 0:
                saldo += valor;
                now = datetime.now();
                formated_data = now.strftime("%d/%m/%Y, %H:%M:%S");
                extrato += f"Depósito: R$ {valor:.2f} realizado em {formated_data}.\n";
                print("\nDepósito realizado com Sucesso.");
                operacoes += 1;
                concluido = True;

            else:
                print("\nOperação falhou. O valor informado é inválido.");



    elif opcao == "s":
        if operacoes < LIMITE_OPERACOES:
            concluido = False;
        
        else:
            print("Número de operações diárias excedido.");
            concluido = True;

        # roda até um valor válido ser informado
        while not concluido :
            valor = float(input("\nInforme o valor do saque ou difite '0' para voltar: "));

            if valor == 0:
                break;

            if valor > saldo:
                print("\nOperação falhou. Saldo Insuficiente.");

            elif valor > limite:
                print("\nOperação falhou! O valor do saque excede o limite.");

            elif numero_saques >= LIMITE_SAQUES:
                print("\nOperação falhou! Número máximo de saques excedido.");

            elif valor > 0:
                saldo -= valor;
                now = datetime.now();
                formated_data = now.strftime("%d/%m/%Y, %H:%M:%S");
                extrato += f"Saque: R$ {valor:.2f} realizado em {formated_data}.\n";
                print("\nSaque realizado com Sucesso.");
                numero_saques += 1;
                operacoes += 1;
                concluido = True;

            else:
                print("Operação falhou! O valor informado é inválido.");

    elif opcao == "e":
        print("\n================ EXTRATO ================");

        # confere se há movimentações na conta
        if extrato: 
            print(extrato);
        
        else:
            print("Não foram realizadas movimentações.\n");
        

        print(f"Saldo: R$ {saldo:.2f}");
        print("==========================================");

    elif opcao == "q":
        break;

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.");