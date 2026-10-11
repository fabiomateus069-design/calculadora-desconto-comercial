#1. ENTRADADA DOS DADOS
print("\n===Seja bem-vindo as lojas Mendonça===")
valor_compra = float(input("Digite o valor da sua compra: R$ "))

print("\nEscolha a forma de pagamento:")
print("1 - À vista / PIX (10% de desconto)")
print("2 - Cartão de credito / Boleto (sem desconto)")

opcao_pagamento = input("Digite o número correspondente a forma de pagamento da sua preferencia: ")


#2. PROCESSAMENTO DOS DADOS
if opcao_pagamento == "1":
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print(f"Você recebeu um desconto de 10% no valor da sua compra. O valor final a ser pago é: R${valor_final:.2f} Obrigado pela sua preferencia!")
elif opcao_pagamento == "2":
    valor_final = valor_compra
    print(f"valor final a ser pago é: R${valor_final:.2f} Obrigado pela sua preferencia!")

print("\n===compra finalizada com sucesso===")
print("===Volte sempre!===")