from validate_docbr import CPF, CNPJ


class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos incorreta!")


class DocCpf:

    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return CPF().mask(self.cpf)

    def valida(self, documento):
        return CPF().validate(documento)


class DocCnpj:

    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")

    def __str__(self):
        return CNPJ().mask(self.cnpj)

    def valida(self, documento):
        return CNPJ().validate(documento)
