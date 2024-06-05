class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo

    # Método getter para o saldo
    def get_saldo(self):
        return self.__saldo

    def verificar_saldo(self):
        saldo = self.__saldo
        if saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

# Classe UsuarioTelefone:
class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.__nome = nome
        self.__plano = plano

    def verificar_saldo(self):
        mensagem = self.__plano.verificar_saldo()
        return mensagem

# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)