class Help:
    def __init__(self, command:str):
        self.command = command

    def get_Help(self):
        match self.command.upper():
            case 'ROLL':
                return """\
                Você pode usar o comando roll utilizando a notação de dados e somando ou subtraindo um bonus.
                    Exemplos:
                        -N30 roll 1d6:    (rola um dado de seis lados)
                        -N30 roll 2d8:    (rola dois dados de oito lados)
                        -N30 roll 2d6+2:  (rola dois d6 e soma 2 ao total)
                        -N30 roll 3d10-2: (rola três dados de dez lados e subtrai 2 ao total
                """
            case 'ROLLRITUAL':
                return """\
                Você pode usar o comando rollRitual utilizando a notação de "Nome" e "Nivel".
                    Exemplos:
                        -N30 rollRitual descarnar normal:     (rola descarnar no nivel normal)
                        -N30 rollRitual descarnar discente:   (rola descarnar no nivel discente)
                        -N30 rollRitual descarnar verdadeiro: (rola descarnar no nivel verdadeiro)
                """
            case _:
                return "Comando não existente"
