from abc import ABC, abstractmethod
class Usuario(ABC):
    """Classe abstrata: base para Cliente e Bibliotecario"""
    def __init__(self, codigo, nome, login, senha):
        self.__codigo = codigo
        self.__nome = nome
        self.__login = login
        self.__senha = senha

    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getSenha(self):
        return self.__senha

    def setSenha(self, senha):
        self.__senha = senha

    def validarAcesso(self, login, senha):
        """Retorna True se login e senha conferem"""
        return self.__login==login and self.__senha==senha

    @abstractmethod
    def getTipo(self):
        pass

    @abstractmethod
    def exibirMenu(self, biblioteca):
        pass

    @abstractmethod
    def visualizarEmprestimos(self, biblioteca):
        pass

    def __str__(self):
        return f"{self.getTipo()}: {self.__nome} (código {self.__codigo})"