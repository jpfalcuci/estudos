##### CLASSES #####

""" classes python e paradigmas
    paradigma procedural (procedimentos): criação de funções que recebem parâmetros, realizam algo e dão um retorno
    este método sofre com desorganização e repetição de código
    paradigma de orientação a objetos nasceu para resolver problemas de organização do paradigma procedural
    este novo paradigma nos incentiva a agrupar funcionalidades relacionadas em um mesmo lugar
    evita a repetição de código, e favorece a reaplicação

    a Classe fica dentro de um 'módulo' (arquivo.py) - em outras linguagens também chamado de 'package' ou 'namespace'; um módulo pode ter uma ou mais sintaxes
    na criação de uma Classe, podemos informar as características, ou 'atributos'
    por convenção, utiliza 'PascalCase'
    atributos e métodos que recebem '__' em sua criação, são atributos privados (por convenção), não devem ser acessados diretamente (apesar de ser possível); só devem ser acessados através dos métodos
    atributos privados mudam a forma de serem chamados diretamente, 'name mangling', resultando em: 'método._Classe__atributo' """


### FUNÇÕES ###

dir()           # retorna uma lista com todos os métodos e atributos de um objeto ou classe

isinstance()    # verifica se um objeto é uma instância ou subclasse de uma classe/tipo
                # isintance(objeto, classe/tipo)

max()           # retorna o maior valor de um item em um iterável ou em comparação com itens
                # key= função de comparação do iterável (maior valor, maior comprimento, probabilidade)



class Usuario():
    def __init__(self, id, user, age, value):
        # função construtora, executada automaticamente ao criar a classe; recebe parâmetros para criar atributos
        # 'self' é a referência que sabe encontrar o objeto construído em memória
        # atributos privados não são herdados naturalmente para as classes filhas devido ao 'name mangling' (_Classe__atributo)
        # por convenção, para evitar o o 'name mangling', usa-se um '_' apenas simbolizando que é um atributo privado 
        self.__id = id          # cria atributos
        self._user = user       # variáveis disponíveis para as classes filhas
        self._age = age
        self._value = value

    # funções relacionadas a uma Classe são chamadas de 'métodos'; ações que o objeto 'sabe fazer'
    def passa_o_ano(self):
        self._age += 1

    def get_idade(self):    # 'getters' devolvem algo, usam 'get_'
        return self._age

    def set_altera_nome(self, user):  # 'setters' atribuem albo, usam 'set_'
        self._user = user

    def aumenta_valor(self, value):
        self._value += value

    def diminui_valor(self, value):
        x = self._value - value
        if self.__valida_valor(x):     # acessa um método privado do próprio objeto
            self._value -= value
        else:
            print('O valor não pode ser inferior a 1000')

    def __valida_valor(self, x):   # método privado
        return x >= 1000

    def __str__(self):
        # espera o retorno de uma string que represente o objeto; objeto da Classe pode ser chamado com print()
        return f'Usuário {self._user}, {self._age} anos, id:{self.__id} e valor {self._value}'

    def __repr__(self):
        # voltado para o desenvolvedor; substitui '__str__' (se não existir)
        return f'Usuario(id={self.__id}, user={self._user}, age={self._age}, value={self._value})'

    def __eq__(self, other):
        # por padrão o python a comparação usa a identidade/endereço do objeto na memória
        if type(other) != Usuario:
            # comparação para verificar se objetos são da mesma classe
            return False
        if not isinstance(other, Usuario):
            # comparação para verificar hierarquia de classes; isintance() retorna True se objeto for de alguma classe subordinada
            return False
        return self._value == other._value    # define condição de igualdade dos objetos (objetos também responderão à '!=')


# herança é o conceito usado quando uma classe herda características de uma 'classe mãe', ou 'super classe'(geralmente mais genéricas)
# classe filha pode sobrescrever métodos da classe mãe e/ou adicionar novos
class UsuarioFilial(Usuario):   # nova classe que herda da classe 'Mae'
    def __init__(self, id, user, age, value, extra):
        # função usada para referenciar métodos da 'classe mãe'
        super().__init__(id, user, age, value)
        self.__extra = extra

    # '@' em palavras chaves são chamados de 'decorators'
    # definindo o atributo como 'Propriedade', funciona como um 'getter'
    # define uma função usando o mesmo nome do atributo, usando a sintaxe com '@property'; deve ser chamado sem o uso de '()'
    @property
    def valor(self):
        return self._value  # acessando atributo criado pela classe mãe

    # só é possível atribuir um '.setter' após o 'atributo' ter sido definido como 'Propriedade' antes
    @valor.setter
    def valor(self, value):
        self._value = value

    # 'método estático' pode ser usado sem um objeto instanciado
    # deve usar com cuidado, mas em alguns casos podem ser úteis, como por exemplo quando existe algo compartilhado entre todos os objetos da mesma classe
    @staticmethod   # não necessita 'self' pois não usa recursos da classe diretamente (quando precisar, utilizar '@classmethod')
    def codigos_filial():
        return {'a': 1, 'b': 2}


joao = Usuario(18, 'João', 29, 2000)
id(joao)            # retorna a identidade/endereço do objeto
joao                # Usuario(id=18, user=João, age=29, value=2000); repr(joao)
joao.passa_o_ano()
joao.get_idade()            # 30
joao.diminui_valor(1500)    # O valor não pode ser inferior a 1000
joao.aumenta_valor(500)
joao.set_altera_nome('João Paulo')
print(joao)         # Usuário João Paulo, 30 anos, id:18 e valor 2500

maria = UsuarioFilial(28, 'Maria', 25, 2000, 'extra')
maria.valor = 2500  # 
maria.valor         # 2500

joao == maria       # True (__eq__)

codigos = UsuarioFilial.codigos_filial()
codigos     # {'a': 1, 'b': 2}



### CLASSES ABSTRATAS ###
# são úteis para definir obrigatoriedade na implantação de métodos; retornam aviso de erro logo no ato de instanciar um objeto

from abc import ABCMeta, abstractmethod
# metaclasse, define a classe como abstrada, não poderá ser instanciada diretamente se tiver um @abstractmethod
class Mae(metaclass=ABCMeta):
    def __init__(self):
        self._param = 0

    @abstractmethod     # obriga as classes filhas a terem este método implantado
    def metodo_abstrato(self):
    # método abstrato obriga que todas as classes filhas implantem e sobrescrevam este método
    # classe filha não poderá ser instanciada se não tiver esse método implantado
        pass

class Filha(Mae):
    def passa_o_mes(self):
        self._param += 1

conta = Filha(1)        # Can't instantiate abstract class Filha with abstract method metodo_abstrato
conta.metodo_abstrato() # name 'conta' is not defined



### POLIMORFISMO ###

# é possível criar uma lista com objetos de diferentes classes, e chamar funções que eles tem em comum, 'duck typing'
# pode reduzir a duplicação de códigos, por ex.: reduz a qtd de 'if' pois não precisa verificar o tipo classe
from operator import attrgetter # método para acessar atributos de um objeto
from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo, self._saldo = codigo, 0
    def deposita(self, valor):
        self._saldo += valor
    @abstractmethod     # obriga as classes filhas a terem este método implantado
    def passa_o_mes(self):
        pass
    def __str__(self):
        return f"[>>Codigo {self._codigo}, Saldo {self._saldo}<<]"

class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)

contas = [conta17, conta16] # lista com objetos de classes diferentes
for conta in contas:
    conta.passa_o_mes()     # duck typing, executa o método que os objetos possuem, mesmo sendo diferentes
    print(conta)            # [>>Codigo 17, Saldo 1007.0<<] / [>>Codigo 16, Saldo 998<<]

for conta in sorted(contas, key=attrgetter('_saldo')):  # retorna a representação de cada conta, ordenando pelo '_saldo', porém cuidados ao acessar atributos privados
    print(conta)                                        # [>>Codigo 16, Saldo 998<<] / [>>Codigo 17, Saldo 1007.0<<]



### MÉTODO DE CLASSE ###

class Mae:
    def __init__(self, nome, valor):
        self._nome = nome
        self.valor = valor

    # criando um 'método de classe', não precisa de objeto para ser usado, podendo ser chamado direto da classe
    # exemplo: contar quantos objetos foram instanciados naquela classe (não faz sentido ter esse método nos objetos)
    @classmethod
    def metodo_classe(cls):
        # diferente do @staticmethod, leva a classe em consideração, chamando explicitamente usando o 'cls' (por convenção, mesmo efeito de 'self')
        return f'Fui chamado pela classe {cls.__name__}'    # tem acesso aos atributos da classe

class Filha1(Mae):          # nova classe que herda da classe 'Mae'
    def __init__(self, nome, valor, atr):
        # função 'super()' é usada para referenciar métodos da 'classe mãe'
        super().__init__(nome, valor)       # passa os atributos recebidos a classe 'Mae'
        self.atr1 = atr

    def __str__(self):    # método específico desta classe
        return f'este objeto tem nome {self._nome} e valor {self.valor}'

class Filha2(Mae):          # outra classe que herda da classe 'Mae'
    def __init__(self, nome, valor, atr):
        super().__init__(nome, valor)       # passa os atributos recebidos a classe 'Mae'
        self.atr2 = atr

    def __str__(self):    # método específico desta classe
        return f'este objeto tem nome {self._nome} e valor {self.valor}'

    def __repr__(self):    # método específico desta classe
        return f'Filha2(nome={self._nome}, valor={self.valor}, atr={self.atr2})'

filha2 = Filha2('ana', 18, 'atributo')
print(filha2)                   # retorna o conteúdo do método '__str__'
repr(filha2)                    # __repr__ = Filha2(nome=ana, valor=18, atr=atributo)
if hasattr(filha2, 'atr2'):     # 'has attribute', consulta se existe o atributo no objeto informado
    print(f'existe o atributo "atr2"')



### HERANÇA DE CLASSES BUILT-IN ###

class Colecao1(list):               # classe que herda da classe 'list' (nativa)
    def __init__(self, nome, lista):
        self.nome = nome
        super().__init__(lista)     # recebe uma lista de objetos que serão iteráveis
# porém, herdar uma classe built-in como uma 'list', pode ser problemático pois não temos controle sobre todos os métodos e comportamentos disponíveis em 'list'
# pra isso, podemos tornar a classe iterável, tendo controle sobre seus métodos

class Colecao2:
    def __init__(self, nome, iter):
        self.nome = nome
        self._iter = iter           # 'iter' representa um iterável, podendo ser lista, tupla, set, dict
    
    def __getitem__(self, i):       # método que define objetos da classe como iteráveis
        return self._iter[i]        # 'i' sendo o índice passado ao objeto instanciado na classe


from abc import ABC
#  abc => abstract base classes, são classes abstratas que podem ser importadas no python com comportamentos já predefinidos

from collections.abc import MutableSequence, Sized
from numbers import Complex
# ao tentar instanciar novos itens em classes genéricas, o console avisará quais métodos deverão ser implantados para que a classe funcione como esperado
class Generica(MutableSequence):
    pass

# herança múltipla
class Classe0():
    pass
class Classe1(Classe0):
    pass
class Classe2(Classe0):
    pass
class HerancaMultipla(Classe1, Classe2):    # herda de múltiplas classes
    # quando as classes possuem mesmos métodos a serem chamados, existe uma ordem na verificação
    # própria classe > 1ª classe mãe > classe 'vó_1' > 2ª classe mãe > classe 'vó_2'
    # se houver outra classe mãe que também é filha da classe 'vó' da 1ª classe mãe, então ela será chamada antes da classe 'vó'
    # o resultado seria => própria classe > 1ª classe mãe > 2ª classe mãe > classe 'vó'
    pass

class MixIn():
    # classes mixin são classes com pequenos trechos de códigos que podem ser necessários em diversas classes, sem precisar implementar individualmente, e não precisam ser instanciadas
    # duas situações principais em que são usados:
    # 1 - fornecer muitos recursos opcionais para uma classe
    # 2 - usar um recurso específico em várias classes diferentes
    pass


### MÉTODOS ESPECIAIS ###
# métodos que não são chamados diretamente
# 'dunder methods' (double underscore), representados por dois '__' antes e depois
"""
python data model
inicialização           __init__
representação           __str__, __repr__
container, sequencia    __contains__, __iter__, __len__, __getitem__
numéricos               __add__, __sub__, __mul__, __mod__
"""
from functools import total_ordering    # método para usar comparadores complexos entre objetos da classe como o '<=', obrigatório ter implementado o '__eq__' e '__lt__'
# este método facilita o uso de comparadores, porém deve-se observar a performance e processamento
# nesses casos, considerar o uso dos 6 métodos da 'rich comparison'
@total_ordering # declaração feita na declaração da classe
class Especiais:
    def __init__(self, parametros):
        # '__init__' é uma função construtora, inicializador, executada automaticamente ao criar a classe
        self.parametros = parametros    # inicializa as variáveis
        self._lista = []                # inicializa uma lista vazia

    def add(self, i):
        self._lista.append(i)            # função adicionar itens a lista criada

    def __str__(self):
    # '__str__' espera o retorno de um valor em string que representa o objeto
    # o objeto instanciado em uma classe com esse método pode ser 'impresso' com print()
        return f'esta é uma representação deste objeto {self}'

    def __repr__(self):
    # similiar ao __str__, mas tem seu uso voltado para o desenvolvedor
    # também devolve uma string, é impresso com print() no lugar do __str__ caso ele não tenha sido declarado
    # fora do print, chamando diretamente o objeto, substitui a representação padrão que mostra o endereço de memória
        return f'Classe(nome={self}, valor={self})'

    def __getitem__(self, i):
    # método que define objetos da classe como iteráveis, e passam a poder receber índice 'objeto[i]'
    # 'Duck typing' = não se preocupa com a tipagem do item e sim com as características e o comportamento
        return self._lista[i]

    def __len__(self):
    # método que retorna o comprimento de um objeto; len(objeto_desta_classe)
        return len(self._lista)

    def __eq__(self, other):
    # por padrão, ao comparar um objeto da classe com o outro (==), o python vai comparar a identidade do objeto, endereço na memória
    # este método permite comparações de igualdade entre o conteúdo dos objetos
        if type(other) != Especiais:
            return False
            # exemplo de comparação inicial para verificar se objetos tem a mesma classe, pode ser útil em alguns casos
            # neste caso, é feita uma comparação específica para a classe informada, sem abranger classes subordinadas
        if not isinstance(other, Especiais):
            return False
            # outro exemplo de comparação, mas dessa vez abrange também a hierarquia da classe informada, 'isinstance' retornará True se o objeto informado for de alguma classe subordinada a classe informada, e o 'not' inverterá a condição
            # 'se não for da classe ou de alguma subordinada, False'
        return self.parametros == other.parametros  # verifica a condição de igualdade
    # este método também responderá ao 'diferente', '!='


    def __lt__(self, other):    # less-than
        if self.parametros != other.parametros:         # verifica se não são iguais
            return self.parametros < other.parametros   # entra na comparação
        return self.parametros < other.parametros       # entra na comparação de 'desempate'
        # verifica se o próprio objeto é menor que o outro, usando um parâmetro de comparação
        # permite também usar o sorted() no objeto da classe, objetos passam a ser ordenáveis
        # existe também o método contrário '__gt__', que usa o comparador '>', porém o uso de um, dispensa o uso do outro
    
    """ rich comparison
    __eq__(), chamado pelo operador ==
    __ne__(), chamado pelo operador !=
    __gt__(), chamado pelo operador >
    __lt__(), chamado pelo operador <
    __ge__(), chamado pelo operador >=
    __le__(), chamado pelo operador <= """

'__len__' in dir(object)    # verifica se existe o método no objeto ou classe

""" if(__name__ == '__main__'):
    executa() => código inteiro do arquivo deve estar dentro dessa função
quando executamos um arquivo python, internamente ele cria a variável __name__ e preenche com o valor '__main__'
nesse exemplo, a executa() só é executada quando o arquivo é executado diretamente
quando o arquivo é importado por outro, a executa() só será executada se for chamada """
