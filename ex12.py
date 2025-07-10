lar = float(input("Altura da parede:"))
alt = float(input("Largura da parede:"))
area = lar * alt 
print ('Sua parede tem a dimensão de {} x {} e sua area é de {} m²'.format(lar, alt, area))
tinta = area / 2
print ('Para pintar essa parede você precisará de {}L de tinta'.format(tinta))