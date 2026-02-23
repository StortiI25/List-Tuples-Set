produtos = []

while True:
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Valor total em estoque')
    print('4 - Mudar quntidade')
    print('5 - Sair')

    opcao = input('Escolha sua opção: ')

    if opcao == "1":
        nome = str(input('Digite o nome do produto: '))
        valor = float(input('Digite o valor do produto: '))
        quantidade = int(input('Digite a quantidade no estoque: '))
    
        produto = {
        'nome': nome,
        'valor': valor,
        'quantidade': quantidade
        }
        produtos.append(produto)
        print('Produto cadastrado com sucesso!\n')

    elif opcao == "2":
        for produto in produtos:
            print(f'{produto}\n')
            
    elif opcao == "3":
        total = 0
        for produto in produtos:
            total += produto['valor'] * produto['quantidade']

        print(f'Valor Total dos produtos são: {total}\n')

    elif opcao == "4":
        
        if not produtos:
            print('Estoque vazio!\n')
        else:
            print("\nProdutos disponíveis:")
            for produto in produtos:
                print(f"- {produto['nome']} (Qtd: {produto['quantidade']})")

            nome_busca = input('\nQual o nome do produto: ')
            encontrado = False

            for produto in produtos:
                if produto['nome'].lower() == nome_busca.lower():
                    nova_qtd = int(input('Nova quantidade: '))
                    produto['quantidade'] = nova_qtd
                    print('Estoque atualizado!\n')
                    encontrado = True

            if not encontrado:
                print('Produto não encontrado\n')

    elif opcao == "5":
        print('Saindo....')
        break


