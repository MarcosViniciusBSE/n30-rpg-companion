class Help:
    def __init__(self, comando:str):
        self.comando = comando

    def get_Help(self):
        match self.comando.upper():
            case 'ROLL':
                return """\
                Você pode usar o comando roll utilizando a notação de dados e comando ou subtraindo um bonus.
                    Exemplos:
                        -1d6:    (rola um dado de seis lados)
                        -2d8:    (rola dois dados de oito lados)
                        -2d6+2:  (rola dois d6 e soma 2 ao total)
                        -3d10-2: (rola três dados de dez lados e subtrai 2 ao total
                """
            case _:
                return "Comando não existente"
