"""
Payment Method Calculator

Task:
Calculate final purchase price based on different payment methods with:
- Cash discounts
- Installment options
- Interest rates for extended installments

Behavior:
[1] 10% cash discount
[2] 5% card discount
[3] 2x no interest
[4] 3x+ with 20% interest

Key Concepts:
- Conditional payment logic
- Percentage calculations
- Installment planning
- Input validation

Example Outputs:
1 → "Sua compra de R$ 100.00 vai custar R$ 90.00 no final"
4 → "Sua compra será parcelada em 5x de R$ 24.00 COM JUROS"
"""

preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
      [1] à vista dinheiro/cheque
      [2] à vista cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

# Definindo o valor total de acordo com a opção de pagamento
if opcao == 1:
    total = preco - (preco * 10 / 100)  # 10% de desconto
    print(f'Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final.')
elif opcao == 2:
    total = preco - (preco * 5 / 100)  # 5% de desconto
    print(f'Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final.')
elif opcao == 3:
    total = preco  # Preço sem desconto
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f} SEM JUROS.')
    print(f'O valor total da compra é R$ {total:.2f}.')
elif opcao == 4:
    total = preco + (preco * 20 / 100)  # 20% de juros
    parcelas = int(input('Quantas parcelas? '))
    parcela = total / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R$ {parcela:.2f} COM JUROS.')
    print(f'O valor total da compra será R$ {total:.2f}.')
else:
    print('Opção inválida de pagamento!')
