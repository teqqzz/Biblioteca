# Sistema de Gerenciamento de Biblioteca

Sistema em Python para controle e administração de um acervo de livros em uma biblioteca comunitária. O projeto foi desenvolvido utilizando o padrão de arquitetura MVC (Model-View-Controller) e conceitos fundamentais de Orientação a Objetos.

---

## 📌 Funcionalidades

- **Cadastrar livro:** Registra um novo livro com código único, título, autor e ano de publicação.
- **Consultar livro:** Busca e exibe os detalhes de um livro específico através do seu código.
- **Listar todos os livros:** Exibe o relatório de todos os livros cadastrados no acervo.
- **Realizar empréstimo:** Altera o status do livro para "Emprestado" (impede empréstimo se já estiver indisponível).
- **Realizar devolução:** Retorna o status do livro para "Disponível".
- **Excluir livro:** Remove um livro da lista (impede a exclusão se estiver emprestado).
- **Encerrar sistema:** Finaliza a execução do programa com segurança.

---

## 🛠️ Requisitos Técnicos Atendidos

- **Orientação a Objetos:** Classe `Livro` com atributos, métodos operacionais (`emprestar`, `devolver`, `exibir_dados`) e controle de status.
- **Lista:** Estrutura dinâmica (`self.biblioteca = []`) para armazenamento dos objetos.
- **Dicionário:** Método `para_dicionario()` que organiza os atributos do livro em chave-valor.
- **Tratamento de Exceções:** Validação de entradas numéricas (`ValueError`), livros não encontrados (`LookupError`) e restrições de regras de negócio (livro já emprestado, código duplicado).
- **Estruturas de Controle:** Laços de repetição (`while`, `for`) e desvios condicionais (`if`, `elif`, `else`).

---

## 📁 Estrutura do Projeto

```text
├── models.py       # Definição da classe Livro e regras da entidade
├── views.py        # Interface de console, captura de dados e exibição de mensagens
├── controllers.py  # Regras de negócio, fluxo do sistema e manipulação da lista
├── main.py         # Arquivo principal para inicialização da aplicação
└── README.md       # Documentação do projeto

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.10 ou superior instalado no sistema.

### Passo a Passo
1. Clone ou baixe todos os arquivos do projeto no mesmo diretório.
2. Abra o terminal ou prompt de comando na pasta do projeto.
3. Execute o comando:

```bash
python main.py