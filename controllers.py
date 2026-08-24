from models import Livro
from views import BibliotecaView

class BibliotecaController:
    # Cria a lista que armazena os livros e instancia a view
    def __init__(self):
        self.biblioteca: list[Livro] = []
        self.view = BibliotecaView()

    def buscar_livro_por_codigo(self, codigo: int) -> Livro:
        # Procura um livro pelo código e retorna o objeto encontrado
        for livro in self.biblioteca:
            if livro.codigo == codigo:
                return livro
        raise LookupError(f"Livro com código {codigo} não foi encontrado.")

    def cadastrar_livro(self) -> None:
        # Valida duplicidade, cria o objeto Livro e adiciona na lista
        try:
            codigo, titulo, autor, ano = self.view.ler_dados_livro()
            for livro in self.biblioteca:
                if livro.codigo == codigo:
                    raise ValueError(f"Já existe um livro cadastrado com o código {codigo}.")

            novo_livro = Livro(codigo, titulo, autor, ano)
            self.biblioteca.append(novo_livro)
            self.view.exibir_mensagem(f"Livro '{titulo}' cadastrado com sucesso!")
        except ValueError as erro:
            self.view.exibir_erro(str(erro))

    def consultar_livro(self) -> None:
        # Busca o livro por código e envia os dados para exibição
        try:
            codigo = self.view.ler_codigo_consulta()
            livro = self.buscar_livro_por_codigo(codigo)
            self.view.exibir_livro(livro.exibir_dados())
        except (ValueError, LookupError) as erro:
            self.view.exibir_erro(str(erro))

    def listar_livros(self) -> None:
        # Envia a lista de livros para a view imprimir
        self.view.listar_livros(self.biblioteca)

    def realizar_emprestimo(self) -> None:
        # Busca o livro e executa o método de empréstimo
        try:
            codigo = self.view.ler_codigo_consulta()
            livro = self.buscar_livro_por_codigo(codigo)
            livro.emprestar()
            self.view.exibir_mensagem(f"Empréstimo do livro '{livro.titulo}' realizado com sucesso!")
        except (ValueError, LookupError) as erro:
            self.view.exibir_erro(str(erro))

    def realizar_devolucao(self) -> None:
        # Busca o livro e executa o método de devolução
        try:
            codigo = self.view.ler_codigo_consulta()
            livro = self.buscar_livro_por_codigo(codigo)
            livro.devolver()
            self.view.exibir_mensagem(f"Devolução do livro '{livro.titulo}' realizada com sucesso!")
        except (ValueError, LookupError) as erro:
            self.view.exibir_erro(str(erro))

    def excluir_livro(self) -> None:
        # Remove o livro da lista se ele não estiver emprestado
        try:
            codigo = self.view.ler_codigo_consulta()
            livro = self.buscar_livro_por_codigo(codigo)
            
            if livro.status == "Emprestado":
                raise ValueError("Não é possível excluir um livro que está emprestado.")

            self.biblioteca.remove(livro)
            self.view.exibir_mensagem(f"Livro '{livro.titulo}' removido com sucesso!")
        except (ValueError, LookupError) as erro:
            self.view.exibir_erro(str(erro))

    def iniciar(self) -> None:
        # Loop do menu que processa as ações até o encerramento
        while True:
            self.view.exibir_menu()
            opcao = self.view.ler_opcao()

            if opcao == "1":
                self.cadastrar_livro()
            elif opcao == "2":
                self.consultar_livro()
            elif opcao == "3":
                self.listar_livros()
            elif opcao == "4":
                self.realizar_emprestimo()
            elif opcao == "5":
                self.realizar_devolucao()
            elif opcao == "6":
                self.excluir_livro()
            elif opcao == "7":
                self.view.exibir_mensagem("Encerrando o sistema da biblioteca. Até logo!")
                break
            else:
                self.view.exibir_erro("Opção inválida! Escolha um número de 1 a 7.")