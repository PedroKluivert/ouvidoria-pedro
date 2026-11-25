print("-" * 50)
print("Canal de Ouvidoria".center(50))
print("-" * 50)

reclamacoes = []
opcao = -1

while opcao != 7:
    print("Menu Principal".center(50))
    print("""
1) Listar Reclamações
2) Adicionar Reclamação
3) Pesquisar Reclamação
4) Remover Reclamação
5) Quantidade de Reclamações
6) Substituir Reclamação
7) Sair
""")
    opcao = int(input("Digite sua opção: "))
    print("-" * 50)

    if opcao == 1:
        if len(reclamacoes) > 0:
            print("Reclamações Registradas:")
            for i in range(len(reclamacoes)):
                print(i + 1, "-", reclamacoes[i])
        else:
            print("Não há reclamação registrada!")

    elif opcao == 2:
        reclamacao = input("Digite sua reclamação: ")
        reclamacoes.append(reclamacao)
        print("Reclamação adicionada com sucesso!")

    elif opcao == 3:
        if len(reclamacoes) == 0:
            print("Não há reclamação para ser pesquisada!")

        else:
            pesquisar_reclamacao = input("Digite palavra ou expressão: ")
            reclamacoes_encontradas = []
            for i in range(len(reclamacoes)):
                if pesquisar_reclamacao in reclamacoes[i]:
                    reclamacoes_encontradas.append(i)

            if len(reclamacoes_encontradas) == 0:
                print("Nenhuma reclamação encontrada com a palavra ou expressão!")

            else:
                print(len(reclamacoes_encontradas), "reclamacao(oes) encontrada(s):")
                for i in reclamacoes_encontradas:
                    print(i+1, "-", reclamacoes[i])

    elif opcao == 4:
        if len(reclamacoes) == 0:
            print("Não há reclamação para ser remover!")

        else:
            for i in range(len(reclamacoes)):
                print(i + 1, "-", reclamacoes[i])
            codigo = int(input("Digite número da reclamação a ser removida: "))

            if codigo <= 0 or codigo > len(reclamacoes):
                print("Número inválido")

            else:
                reclamacoes.pop(codigo - 1)
                print("Reclamação removida com sucesso!")

    elif opcao == 5:
        print("Quantidade de reclamações:", len(reclamacoes))

    elif opcao == 6:
        if len(reclamacoes) == 0:
            print("Não há reclamação para substituir!")

        else:
            for i in range(len(reclamacoes)):
                print(i + 1, "-", reclamacoes[i])
            codigo = int(input("Digite código da reclamação a ser substituída: "))
            if codigo <= 0 or codigo > len(reclamacoes):
                print("Código inválido")

            else:
                nova_reclamacao = input("Digite nova reclamação: ")
                reclamacoes[codigo - 1] = nova_reclamacao
                print("Reclamação substituída com sucesso!")

    elif opcao != 7:
        print("Opção inválida!")
    print("-" * 50)

print("Obrigado por usar o sistema!".center(50))
print("-" * 50)