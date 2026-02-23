nota = [7.5, 8.0, 6.5, 9.0, 5.5]

print('-=' *15)
print(f'A maior nota recebida foi: {max(nota)}')
print('-=' *15)
print(f'A media das notas foi: {sum(nota)/5}')
print('-=' *15)
nota.append(10)
print(f'Nota 10 adicionada: {nota}')
print('-=' *15)
print(sorted(nota))
print('-=' *15)
print('Notas Maiores do que 7: ')
for n in nota:
    if n >= 7:
        print(f'{n}', end=' ')