
class Livro:
    def __init__(self, codigo: int, titulo: str, autor: str, ano: int):
        # Inicializa os dados do livro e define o status inicial
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = "Disponível"

    def emprestar(self) -> None:
        # Altera o status para 'Emprestado' se o livro estiver disponível
        if self.status == "Emprestado":
            raise ValueError(f"O livro '{self.titulo}' já está emprestado.")
        self.status = "Emprestado"

    def devolver(self) -> None:
        # Altera o status para 'Disponível' se o livro estiver emprestado
        if self.status == "Disponível":
            raise ValueError(f"O livro '{self.titulo}' já se encontra na biblioteca.")
        self.status = "Disponível"

    def para_dicionario(self) -> dict:
        # Retorna os atributos do livro em formato de dicionário
        return {
            "codigo": self.codigo,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "status": self.status
        }

    def exibir_dados(self) -> str:
        # Formata os dados do dicionário em texto para exibição
        dados = self.para_dicionario()
        return (
            f"Código: {dados['codigo']} | "
            f"Título: {dados['titulo']} | "
            f"Autor: {dados['autor']} | "
            f"Ano: {dados['ano']} | "
            f"Status: {dados['status']}"
        )