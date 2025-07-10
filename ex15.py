d = int(input('Quantos dias alugados?'))
km = float(input('Quantos km rodados?'))
p = (60 * d) + (0.15 * km) 
print ('O total a pagar é de R$ {}'.format(p))