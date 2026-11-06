from model.Usuario import Usuario

class Cliente(Usuario):
    """Cliente: Vê só os próprios empréstimos e pode renová-los"""
    def __init__(self, codigo, nome, login, senha):
        super().__init__(codigo, nome, login, senha)

    def getTipo(self):
        return "Cliente"

    def exibirMenu(self, Biblioteca):
        pass

    def visualizarEmprestimos(self, biblioteca):
        pass

