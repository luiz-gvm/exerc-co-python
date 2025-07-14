def cadastrar_jogador():
    nome = input("Nome do jogador: ")
    idade = input("Idade do jogador: ")
    posicao = input("Posição do jogador: ")

    with open("jogadores.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome},{idade},{posicao}\n")
    
    print("Jogador cadastrado com sucesso!")

def listar_jogadores():
    try:
        with open("jogadores.txt", "r", encoding="utf-8") as arquivo:
            print("\n--- Lista de Jogadores ---")
            for linha in arquivo:
                nome, idade, posicao = linha.strip().split(",")
                print(f"Nome: {nome} | Idade: {idade} | Posição: {posicao}")
    except FileNotFoundError:
        print("Nenhum jogador cadastrado ainda.")

while True:
    print("\nMENU")
    print("1 - Cadastrar jogador")
    print("2 - Listar jogadores")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_jogador()
    elif opcao == "2":
        listar_jogadores()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
