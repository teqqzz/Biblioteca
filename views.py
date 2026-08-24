class BibliotecaView:
    @staticmethod
    def exibir_menu() -> None:
        # Imprime as opções do menu principal no terminal
        print("\n" + "=" * 40)
        print("    SISTEMA DE GERENCIAMENTO DE BIBLIOTECA")
        print("=" * 40)
        print("1. Cadastrar livro")
        print("2. Consultar livro")
        print("3. Listar todos os livros")
        print("4. Realizar empréstimo")
        print("5. Realizar devolução")
        print("6. Excluir livro")
        print("7. Encerrar sistema")
        print("=" * 40)

    @staticmethod
    def ler_opcao() -> str:
        # Captura a opção digitada pelo usuário
        return input("Escolha uma opção (1-7): ").strip()

    @staticmethod
    def ler_dados_livro() -> tuple:
        # Lê e valida os dados de entrada para cadastro do livro
        print("\n--- CADASTRO DE LIVRO ---")
        try:
            codigo = int(input("Digite o código do livro: "))
        except ValueError:
            raise ValueError("Código inválido. O código deve ser um número inteiro.")

        titulo = input("Digite o título do livro: ").strip()
        if not titulo:
            raise ValueError("O título não pode estar vazio.")

        autor = input("Digite o autor do livro: ").strip()
        if not autor:
            raise ValueError("O autor não pode estar vazio.")

        try:
            ano = int(input("Digite o ano de publicação: "))
        except ValueError:
            raise ValueError("Ano inválido. O ano deve ser um número inteiro.")

        return codigo, titulo, autor, ano

    @staticmethod
    def ler_codigo_consulta() -> int:
        # Lê e valida o código informado para busca
        try:
            return int(input("Digite o código do livro: "))
        except ValueError:
            raise ValueError("Código inválido. Digite apenas números.")

    @staticmethod
    def exibir_mensagem(mensagem: str) -> None:
        # Exibe mensagens de sucesso
        print(f"[OK] {mensagem}")

    @staticmethod
    def exibir_erro(mensagem: str) -> None:
        # Exibe mensagens de erro capturadas
        print(f"[ERRO] {mensagem}")

    @staticmethod
    def exibir_livro(detalhes: str) -> None:
        # Exibe os dados formatados de um livro
        print("\n--- DETALHES DO LIVRO ---")
        print(detalhes)

    @staticmethod
    def listar_livros(lista_livros: list) -> None:
        # Percorre a lista e imprime todos os livros
        print("\n--- LISTAGEM DE LIVROS ---")
        if not lista_livros:
            print("Nenhum livro cadastrado na biblioteca.")
            return

        for livro in lista_livros:
            print(livro.exibir_dados())