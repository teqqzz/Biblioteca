from controllers import BibliotecaController

def main():
    # Instancia o controlador e inicia a aplicação
    sistema = BibliotecaController()
    sistema.iniciar()

if __name__ == "__main__":
    # Executa a função principal quando o script é chamado
    main()