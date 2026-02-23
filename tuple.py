produto = ("Notebook", 3500.00, 10)
produto2 = ("Mouse", 150.00, 50)

nome, preco, quantidade = produto
nome2, preco2, quantidade2 = produto2

vt1 = preco * quantidade
vt2 = preco2 * quantidade2

print(f'Produto em Promoção: {nome}')
print(f'De 5000.0 para: {preco}')
print(f'Só restão apenas {quantidade} Unidades')
print(f'Valor total em estoque: {vt1}')
#produto[1] = (4000.0)

print(f'-=' *15)

print(f'Produto em Promoção: {nome2}')
print(f'De 500.0 para: {preco2}')
print(f'Só restão apenas {quantidade2} Unidades')
print(f'Valor total em estoque: {vt2}')

print(f'-=' *15)

if vt1 > vt2:
    print(f'O valor em estoque do {nome} é maior do que {nome2}')
elif vt2 > vt1:
    print(f'O valor em estoque do {nome2} é maior do que {nome}')
else:
    print(f'O {nome} tem o mesmo valor do que {nome2}')
