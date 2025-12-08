# sistema_biblioteca.py

class Livro:
    """Representa um livro na biblioteca."""
    def __init__(self, titulo: str, autor: str, isbn: str):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn})"

class Biblioteca:
    """Gerencia a coleção de livros e os empréstimos."""
    def __init__(self):
        self.colecao_livros = [] # Lista de objetos Livro
        self.emprestimos = {}    # Dicionário: {isbn: nome_leitor}

    def adicionar_livro(self, livro: Livro):
        """Adiciona um livro à coleção."""
        self.colecao_livros.append(livro)
        print(f"Livro adicionado: {livro.titulo}")

    def emprestar_livro(self, isbn: str, leitor: str):
        """Realiza o empréstimo de um livro pelo ISBN."""
        for livro in self.colecao_livros:
            if livro.isbn == isbn:
                if livro.disponivel:
                    livro.disponivel = False
                    self.emprestimos[isbn] = leitor
                    print(f"\nEmpréstimo realizado: '{livro.titulo}' para {leitor}.")
                    return
                else:
                    print(f"\nErro: O livro '{livro.titulo}' já está emprestado para {self.emprestimos.get(isbn, 'outro leitor')}.")
                    return
        print(f"\nErro: Livro com ISBN {isbn} não encontrado.")

    def devolver_livro(self, isbn: str):
        """Registra a devolução de um livro pelo ISBN."""
        if isbn in self.emprestimos:
            for livro in self.colecao_livros:
                if livro.isbn == isbn:
                    livro.disponivel = True
                    del self.emprestimos[isbn]
                    print(f"\nDevolução realizada: O livro '{livro.titulo}' agora está disponível.")
                    return
        else:
            print(f"\nErro: Livro com ISBN {isbn} não estava registrado como emprestado.")
    
    def listar_status(self):
        print("\n--- Status Atual da Biblioteca ---")
        print(f"Livros na coleção: {len(self.colecao_livros)}")
        print(f"Livros emprestados: {len(self.emprestimos)}")
        
        for livro in self.colecao_livros:
            status = "Disponível" if livro.disponivel else f"Emprestado para {self.emprestimos.get(livro.isbn, 'Desconhecido')}"
            print(f"- {livro.titulo}: {status}")


# --- Demonstração do Sistema ---
biblioteca_municipal = Biblioteca()

# 1. Adicionar livros
livro1 = Livro("Python para Todos", "Dr. Chuck", "12345")
livro2 = Livro("Dom Casmurro", "Machado de Assis", "67890")

biblioteca_municipal.adicionar_livro(livro1)
biblioteca_municipal.adicionar_livro(livro2)

# 2. Listar status inicial
biblioteca_municipal.listar_status()

# 3. Realizar empréstimos
biblioteca_municipal.emprestar_livro("12345", "Alice")
biblioteca_municipal.emprestar_livro("67890", "Bob")

# 4. Tentar emprestar livro já emprestado
biblioteca_municipal.emprestar_livro("12345", "Charlie")

# 5. Listar status após empréstimos
biblioteca_municipal.listar_status()

# 6. Devolver um livro
biblioteca_municipal.devolver_livro("12345")

# 7. Listar status final
biblioteca_municipal.listar_status()