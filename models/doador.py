from models.usuario import Usuario


class Doador(Usuario):
    def __init__(self,nome,email,senha):
        super().__init__(nome,email, senha)
        self.historico_doacoes = []

    def registrar_doacao(self, material):
        self.historico_doacoes.append(material)
        print(f"Obrigado, {self.nome}! {material} doado com sucesso")