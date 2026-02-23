jogador = {
    "nome": "Carlos",
    "nivel": 5,
    "vida": 100,
    "ataque": 30
}

print(f'O Jogador se chama: {jogador["nome"]}')
print(f'O Nivel do jogador é: {jogador["nivel"]}')
jogador['nivel'] = 6
print(f'O jogador Subil de nivel: {jogador["nivel"]}')
jogador['defesa'] = 20
for chave, valor in jogador.items():
    print(chave,'-', valor)