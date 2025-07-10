num = int(input('Digite um numero:'))
print('Escolha a base de conversão: ')
print('1 para binário')
print('2 para octal')
print('3 para hexadecimal')

escolha = int(input('sua escolha:'))

if escolha == 1:
    print(bin(num)[2:])
elif escolha == 2:
    print(oct(num)[2:])
elif escolha == 2: 
    print(hex(num)[2:])
else: 
    print('Escolha inválida. por favor, tente novamente.')