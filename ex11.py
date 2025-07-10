a = float(input('digite o preço do produto: R$'))
p = a * 0.05 
v = a - p
print ('O preço com desconto de 5% ficara R${}'.format(v))

preco = float(input('Qual p preço do produto? R$'))
novo = preco - (preco * 5 / 100)
print ('O produto que custava R$ {}, na promoção vai custar R${}'.format(preco, novo))