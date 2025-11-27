# main.py

from models.carro import Carro


MARCAS_E_MODELOS = {
    "Fiat": ["Uno", "Argo", "Mobi", "Cronos"],
    "Chevrolet": ["Onix", "Tracker", "Spin"],
    "Volkswagen": ["Gol", "Polo", "Nivus", "Jetta"]
}




def menu():
    """Exibe o menu principal e solicita a opção do usuário."""
    print("\n=== SISTEMA DE CADASTRO DE CARROS ===")
    print("1 - Cadastrar carro")
    print("2 - Listar carros")
    print("3 - Excluir carro")
    print("0 - Sair")
    return input("Escolha uma opção: ")


def escolher_marca():
    """
    Melhoria 1: Cria um menu numerado para escolher a marca.
    Retorna a marca escolhida (string).
    """
    print("\n--- ESCOLHER MARCA ---")

    # Mapeamento do número digitado para o nome da marca (ex: 1 -> "Fiat")
    opcoes_marca = {}

    # Lista com apenas os nomes das marcas (chaves do dicionário)
    marcas = list(MARCAS_E_MODELOS.keys())

    # Exibe as opções numeradas
    print("Escolha a marca:")
    for i, marca in enumerate(marcas, 1):
        print(f"{i} - {marca}")
        opcoes_marca[str(i)] = marca  # Salva a marca para ser resgatada pelo número

    # Loop de validação para a escolha
    while True:
        opcao = input("Digite o número da marca: ")
        if opcao in opcoes_marca:
            # Retorna o nome da marca correspondente ao número
            return opcoes_marca[opcao]
        else:
            print("Opção de marca inválida! Por favor, escolha um dos números acima.")


def escolher_modelo(marca_selecionada):
    """
    Melhoria 2: Cria um menu numerado de modelos, filtrando pela marca.
    Retorna o modelo escolhido (string).
    """
    print(f"\n--- ESCOLHER MODELO ({marca_selecionada}) ---")

    # Obtém a lista de modelos para a marca selecionada
    modelos = MARCAS_E_MODELOS.get(marca_selecionada, [])
    opcoes_modelo = {}

    # Exibe as opções numeradas
    print("Escolha o modelo:")
    for i, modelo in enumerate(modelos, 1):
        print(f"{i} - {modelo}")
        opcoes_modelo[str(i)] = modelo  # Salva o modelo para ser resgatado pelo número

    # Loop de validação para a escolha
    while True:
        opcao = input("Digite o número do modelo: ")
        if opcao in opcoes_modelo:
            # Retorna o nome do modelo correspondente ao número
            return opcoes_modelo[opcao]
        else:
            print("Opção de modelo inválida! Por favor, escolha um dos números acima.")


def validar_ano():
    """
    Melhoria 3: Valida se o ano digitado é composto apenas por números.
    Retorna o ano válido (string).
    """
    print("\n--- INFORMAR ANO ---")

    # Loop de validação
    while True:
        ano = input("Ano: ")
        # Verifica se a string contém APENAS dígitos e, idealmente, tem 4 caracteres
        if ano.isdigit() and len(ano) == 4:
            return ano
        else:
            print("❌ Ano inválido! Digite 4 dígitos numéricos (ex: 2023).")


def excluir_carro():
    """Gerencia a lógica de exclusão de um carro (Opção 3)."""
    print("\n--- EXCLUIR CARRO ---")

    carro_modelo = Carro("", "", "")
    lista = carro_modelo.carregar_todos()

    if not lista:
        print("🙁 Nenhum carro cadastrado para excluir.")
        return

    print("Carros cadastrados (Escolha o número para excluir):")
    print("-" * 40)
    for i, c in enumerate(lista, 1):
        print(f"[{i}] {c['marca']} - {c['modelo']} - {c['ano']}")
    print("-" * 40)

    while True:
        try:
            escolha = input("Digite o número do carro a excluir (ou 'c' para cancelar): ")

            if escolha.lower() == 'c':
                print("Operação cancelada.")
                return

            indice_real = int(escolha) - 1

            if carro_modelo.excluir_registro(indice_real):
                print(f"\n🗑️ Carro {escolha} excluído com sucesso!")
                return
            else:
                print("Número inválido! O carro não existe na lista.")

        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números ou 'c'.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return


# --- LOOP PRINCIPAL DO SISTEMA ---
while True:
    opcao = menu()

    if opcao == "1":
        print("\n--- CADASTRAR CARRO ---")

        # Chamada das funções com menus e validação
        marca = escolher_marca()
        modelo = escolher_modelo(marca)
        ano = validar_ano()

        # POO em ação: cria objeto e chama o método da classe Carro
        carro = Carro(marca, modelo, ano)
        carro.salvar_carro()

        print("\n✅ Carro salvo com sucesso!")

    elif opcao == "2":
        print("\n--- LISTA DE CARROS ---")

        # Chama o método de HERANÇA para carregar os dados
        lista = Carro("", "", "").carregar_todos()

        if not lista:
            print("🙁 Nenhum carro cadastrado ainda.")
        else:
            print("-" * 40)
            for c in lista:
                print(f"🚗 {c['marca']} - {c['modelo']} ({c['ano']})")
            print("-" * 40)

    elif opcao == "3":
        excluir_carro()

    elif opcao == "0":
        print("\n👋 Saindo... Até mais!")
        break

    else:
        print("\n❌ Opção inválida! Escolha 1, 2, 3 ou 0.")