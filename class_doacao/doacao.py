from datetime import datetime

class Doacao:
    def __init__(self, id_doacao, id_material, id_beneficiario):
        # Inicializa os dados básicos conforme a Tabela Doação do documento
        self.id_doacao = id_doacao
        self.id_material = id_material
        self.id_beneficiario = id_beneficiario
        
        # Define a data de solicitação automaticamente para o momento atual
        self.data_solicitacao = datetime.now()
        
        # O status inicial é sempre 'solicitado'
        self.status_doacao = 'solicitado'
        
        # A data de entrega começa vazia (None) até ser concluída
        self.data_entrega = None

    def confirmar_entrega(self):
        """Atualiza o status para concluído e marca a data da entrega."""
        self.status_doacao = 'concluido'
        self.data_entrega = datetime.now()
        print(f"Doação {self.id_doacao} concluída com sucesso!")

    def __str__(self):
        # Método para mostrar os dados de forma legível quando der um print()
        return (f"Doação ID: {self.id_doacao} | "
                f"Status: {self.status_doacao} | "
                f"Material ID: {self.id_material}")

