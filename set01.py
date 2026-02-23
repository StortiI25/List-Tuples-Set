nomes = ["Carlos", "Ana", "Carlos", "João", "Ana", "Pedro"]

x = set(nomes)

print(f'Estes são os nomes da lista: {x}')
x.add("Maria")
print('-=' *15)
print(f'Maria foi adcionada ao grupo: {x}')
print('-=' *15)
print("Carlos" in x)
x.add("Carlos")
print('-=' *15)
print(x)