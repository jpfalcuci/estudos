import re


class TelefonesBr:

    def __init__(self,telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número incorreto!")

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self,telefone):
        padrao = "(55)?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao,telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        padrao = "(55)?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        r = re.search(padrao,self.numero)
        numero_formatado = f"+{r.group(1)}({r.group(2)}){r.group(3)}-{r.group(4)}"
        return numero_formatado
