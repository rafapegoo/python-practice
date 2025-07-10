from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar ano atual'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400:
    print ('O ano {} é um ano bissexto'.format(ano))
else: 
    print ('O ano {} NÃO é um ano bissexto'.format(ano))