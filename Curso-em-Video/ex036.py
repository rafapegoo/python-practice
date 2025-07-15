"""
Number Base Converter

Task:
Convert a decimal number to binary, octal, or hexadecimal based on user selection.

Features:
- Takes user input for number and desired base
- Handles invalid menu choices
- Removes Python prefix (0b, 0o, 0x) from converted numbers
- Clean menu interface

Example Usage:
Input: 
Enter a number: 42
Choose conversion:
1 for binary
2 for octal
3 for hexadecimal
Your choice: 2
Output: 
52 (octal representation of 42)

Error Case:
Input:
Your choice: 5
Output:
"Invalid choice. Please try again."

Key Concepts:
- Number base conversions
- String slicing to remove prefixes
- Menu-driven programs
- Input validation
"""

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
