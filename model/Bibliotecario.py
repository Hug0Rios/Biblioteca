from model.Usuario import Usuario

class Bibliotecario(Usuario):
    """Bibliotecario: vê os empréstimos de todos e não renova"""

    def __init__(self, codigo, nome, login, senha):
        super().__init__(codigo, nome, login, senha )

    def getTipo(self):
        return "Bibliotecario"

    def exibirMenu(self, biblioteca):
        pass

    def visualizarEmprestimos(self, biblioteca):
        pass
