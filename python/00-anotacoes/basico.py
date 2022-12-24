""" sobre o python
    - linguagem de propósito geral, mas muito usada para data science, inteligencia artificial, biotecnologia e computação 3d
    - formato de arquivo: 'arquivo.py'
    - todas as funções e estruturas do python devem ser indentadas
    - 'zen of python' é uma coleção de princícios orientadores que influenciam no design da linguagem
    - python utiliza o conceito de 'interpretação', porém, implicitamente o python lê os módulos importados e faz uma 'compilação' para um código 'bytecode', para melhorar o desempenho e execução do ambiente; essa compilação gera os arquivos no diretório __ pycache __ (oculto)
    - bytecode é um código intermediário, normalmente independente do sistema operacional
    - então, o python pode ser considerada uma linguagem híbrida, é interpretada mas existe a compilação implícita
    - o python possui um 'garbage collector', que procura e apaga objetos sem referência/utilização
    - possui suporte a muitas bibliotecas, para pacotes visitar Python Package Index (pypi) => https://pypi.org/
    - comparando, no C é necessário passar o código por um compilador que lê o código fonte e faz uma análise da sintaxe, depois gera um outro arquivo que será executado
    - o arquivo gerado pelo compilador não é executável em S.O.s diferentes do que o que foi gerado, é necessário uma nova compilação no S.O. desejado
    - muitas vezes o código fonte utiliza algo específico do S.O., e passa a depender dele, nesse caso então, uma nova compilação não funcionaria 

- instalação do python:
    - windows
        - https://www.python.org/downloads
        - executar .exe => check Add Python X to PATH => seguir instalação padrão
        - é instalado o console Python e o IDLE Shell
        - prompt de comando:
            - python -V / python --version (mostra a versão instalada do python)
            - python (executa o python, console indicará >>>)
            - ctrl+c sai do console python
    - linux
        - python já vem pré instalado no linux
        - caso não tenha, executar 'sudo apt-get install python3'
        - para atualizar, 'sudo apt-get update'
        - abrir 'bash' e conferir 'python3 -v' (dica: usar 'tab' para autocompletar)
        - python3 executa o python (console também indicará >>>)
        - ctrl+d sai do console python
    - serviços web
        - buscar 'python repl' (interfaces que executam o código python)
        - https://replit.com/ é um dos mais famosos (50+ linguagens)
    - ferramentas IDE
        - Integrated Development Environment, é um conjunto de ferramentas de desenvolvimento de software, possui um editor de código, um depurador, compilador e outros recursos importantes, em uma única ferramenta  """



##### VARIÁVEIS #####

# por convenção usa-se snake_case
# variável só existe quando atribuímos um valor (diferente de outras linguagens); toda variável é um objeto
variavel_exemplo = 'conteúdo que a variável armazenará'
nome, idade = 'João', 29            # declaração múltipla
var_1, var_2 = 'conteúdo1', 'conteúdo2'
var1, var2 = var_2, var_1           # substitui o valor das variáveis, neste caso, trocando entre elas    
var2 = var1                         # nova variável apontando para o mesmo objeto na memória de 'var1'
var2 = None                         # 'nulo', elimina referência da variável



##### FUNÇÕES #####

# exibe na tela
print('Hello world!')                       # Hello world!
print('Hello', 'world', sep=', ', end='!')  # Hello, world!

# ajuda interativa ('q' p/ sair da documentação e ctrl+c ou ctrl+d p/ sair do console 'help')
help()  # console passa a ser 'help>'

# retorna o tipo do objeto
type('Hello')   # str
type(10)        # int
type(1.1)       # float
type(True)      # bool

# solicita e captura uma entrada do usuário e retorna uma string
input('Digite uma entrada: ')
resposta = input('Digite: ')    # atribui a resposta do input a uma variável

# transforma objeto em tipo inteiro, sem arredondar
int('10')   # 10
int(10.2)   # 10
int(10.8)   # 10

# transforma objeto em tipo string
str(10.1)   # '10.1'

# retorna uma sequencia de valores, (início(inclusivo), último(exclusivo), intervalo)
# por padrão começa no 0 e incrementa em 1
range(10)           # 0 1 2 ... 7 8 9
range(0, 11)        # 0 1 2 ... 8 9 10
range(0, 11, 2)     # 0 2 4 6 8 10

# retorna um número inteiro, arredondado
round(1.6666, 2)    # 1.67
round(1.6666, 3)    # 1.667

# retorna um número absoluto, sempre positivo
abs(-1.6666)    # 1.6666

# retorna se o valor informado é True ou False
# valores vazios (0, "" ou 'None')) são considerados False, do contrário são True 
bool(0)     # False
bool(1)     # True


# declaração de novas funções
# variáveis declaradas dentro de funções, só existem dentro da função
# por convenção, usa-se 'snake_case' na declaração

def nova_funcao():
    """ Explicação do que faz a função """
    pass            # permite que uma função exista, mesmo que ainda não haja código pronto p/ ela
    'códigos e/ou outras funções'    
    global var      # variável global, que existirá fora da função ou se refere a variáveis já criadas fora da função 
    var = 1
nova_funcao()       # executa a função
var                 # 1

def soma(a, b):     # define função e parâmetros
    x = a + b       # usa os parâmetros no código
    return x        # retorna um valor (pode retornar mais de um valor)
soma(1 ,2)          # 3

# função lambda (funções anônimas, que não precisam ser definidas e não serão reutilizadas)
# principal vantagem é usar para criar parâmetro para outra função e também usar em iterações (ver laços)
imposto = lambda x: x*1.08
imposto(100)    # 108.0



##### ESTRUTURAS CONDICIONAIS #####

a, b = 10, 20
if (a > b):         # se condição verdadeira, executa código
    print('É maior')
elif (a == b):      # se não, verifica outra condição
    print('São iguais')
else:               # se nenhuma anterior, executa código
    print('Não é maior')


# expressões condicionais (operação ternária)

x = 10
# <expressao1> if <condicao> else <expressao2>
print ("par" if x % 2 == 0 else "impar")    # par
# <condicao> and <expressao1> or <expressao2> (alternativa com valores booleanos)
print (x % 2 == 0 and "par" or "impar")     # par
# sintaxe alternativa
('impar', 'par')[x%2==0]                    # par


""" operadores
aritméticos:
    '+'     adição
    '-'     subtração
    '*'     multiplicação
    '/'     divisão	            retorna um float
    '//'    divisão inteira     retorna um int
    '%'     módulo	            resto da divisão (divisão exata retorna 0)
    '**'    exponenciação
comparação:
    '=='	igual a	            devem ser do mesmo tipo
    '!='	diferente de
    '>'     maior que
    '>='	maior ou igual
    '<'     menor que
    '<='    menor ou igual
atribuição:
    '='	x = 1
    '+='	x = x + 1
    '-='	x = x - 1
    '*='	x = x * 1
    '/='	x = x / 1
    '%='	x = x % 1
lógicos:
    and (&)
    or	(|)
    not (~)
identidade:
    is          verifica se são o mesmo objeto
    is not
associação:
    in          verifica se existe em uma coleção
    not in      """



##### MANIPULAÇÃO DE ARQUIVOS #####

arquivo = open('file.txt', 'w', encoding='utf-8')   # cria um novo arquivo; write(sobrescresve conteúdo existente), read ou append
arquivo.write('conteúdo\n')     # adiciona conteúdo ao arquivo, '\n' pula linha
arquivo.close()                 # fecha o arquivo (é boa prática sempre fechar)
arquivo.read()                  # lê todo conteúdo do arquivo; para o cursor no fim do arquivo (para ler novamente, fechar e reabrir)
arquivo.readline()              # lê uma linha a cada vez que o comando é acionado ('\n' é mostrado por padrão)

# problemas com encoding, caso aconteça 'UnicodeDecodeError'
arquivo.encode('raw_unicode_escape').decode('utf-8') # deve funcionar

# ao abrir um arquivo, podem ocorrer erros de código que façam com que ele não seja fechado (recursos do computador continuam alocados a ele)
# para evitar isso, usa-se 'try' e 'finally', garantindo a finalização
try:
    f = open('teste.txt', 'w')
    f.write('Testando escrita')
finally:
    f.close()

# 'with' tem o mesmo efeito; fecha automaticamente (garante o encerramento dos recursos alocados)
with open('teste.txt', 'w') as f:
    f.write('Testando escrita com with')

import io
arquivo = io.open('file.txt', 'r', encoding='utf-8')
artigos = arquivo.read()

import os
root = os.path.abspath('')          # jupyter notebook
root = os.path.dirname(__file__)    # python script
config_ini = os.path.join(root, 'tools/config.ini')