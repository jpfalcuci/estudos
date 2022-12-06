# módulo matplotlib, biblioteca para geração de gráficos 
# https://matplotlib.org/
# em geral já vem instalada, mas se necessário, instalar com 'pip install matplotlib'
# %matplotlib inline => usar em jupyter notebooks
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (16, 8))     # define o tamanho padrão dos gráficos na tela

provas, notas = list(range(1, 9)), [8, 7, 7, 8, 9, 3, 2, 8]
x, y = provas, notas
plt.title('Notas das provas')   # define o nome do gráfico
plt.xlabel('Provas')            # define o rótulo do eixo 'x'
plt.ylabel('Notas')             # define o rótulo do eixo 'y'

plt.plot(x, y, marker='o')  # cria um gráfico de linhas; marker define o marcador do encontro dos eixos
plt.show()                  # constrói o gráfico

plt.bar(x, y)               # cria um gráfico de barras, pode ser usado em conjunto com outro tipo de gráfico
plt.show()

# comparação de gráficos
x1, y1 = [1, 3, 5, 7, 9], [2, 3, 7, 1, 0]
x2, y2 = [2, 4, 6, 8, 10], [5, 1, 3, 7, 4]
plt.bar(x1, y1, label='Aluno 1')    # gráfico 1
plt.bar(x2, y2, label='Aluno 2')    # gráfico 2
plt.legend()                        # imprime a 'label' definida em bar()
plt.show()
# comparação de dois gráficos com mesmo valor 'x'
# definir 'align' como 'edge' para a barra ficar na borda, e width positivo e negativo, para cada barra ir para um lado do 'align'
plt.bar(x1, y1, width=-0.35, align='edge')
plt.bar(x1, y2, width=0.35, align='edge')

# gráfico de dispersão
x, y = [1, 3, 5, 7, 9], [2, 3, 7, 1, 0]
diam = [300, 150, 400, 100, 70]
# cria um gráfico de dispersão usando pontos
plt.scatter(x, y, label='Minhas notas',  marker='p', color='k', s=diam)
# 'color=' muda a cor dos pontos, 's=' muda o tamanho, pode receber um inteiro ou uma sequência
plt.plot(x, y, color='r', linestyle=':')    # constrói as linhas (opcional)
# 'linestype' muda o tipo da linha
# 'color' pode receber hexadecimal, '#000000'
plt.show()

plt.savefig('grafico.pdf')          # salva o gráfico na mesma pasta onde o arquivo está sendo executado
plt.savefig('grafico.png', dpi=300) # salva em formato png, com 300 de 'dpi'

# importando dados de um .csv
dados = open('arquivo.csv').readlines()
x, y = [], []
for i in range(len(dados)):
    if i != 0:  # ignorando a primeira linha
        linha = dados[i].split(';')
        x.append(int(linha[0]))
        y.append(int(linha[1]))

# histograma, distribuição de frequências dos dados
plt.hist(dados['Valor'])    # retorna um grafico de histograma
dados.hist(['Valor'], by=['Tipo'])

# gráfico de pizza
plt.pie(dados, labels='rótulos', autopct='%1.1f%%', explode = (.1, .1, .1))
# autopct para colocar as porcentagens em cada fatia do gráfico
# explode para destacar as fatias do gráfico

# gráfico boxplot
""" boxplot (diagrama de caixa)
    é uma técnica de visualização de dados onde a representação das variações é feita por meio de quartis
    importante para mostrar o quão dispersos estão os dados
    o retângulo central concentra 50% dos dados
    a linha ao centro indica a mediana
    os círculos representam os outliers (dados muito destoante dos outros) """
vetor = [3, 22, 17, 28, 31, 31, 26, 45, 40, 31]
plt.boxplot(vetor, by='Grupo')      # cria gráfico boxplot através da lista de valores; by= para agrupamento
plt.title('Boxplot')
plt.show()

# # criando estatísticas do box plot
valor = dados['Valor']
Q1 = valor.quantile(.25)    # primeiro quartil
Q3 = valor.quantile(.75)    # terceiro quartil
IIQ = Q3 - Q1               # intervalo interquartil
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ
selecao = (valor >= limite_inferior) & (valor <= limite_superior)
novos_dados = dados[selecao]

# usando um DataFrame pandas
df = 'DataFrame'
fig = df['Coluna'].mean().plot.bar()
fig.set_title('Título do gráfico')
fig.set_ylabel('Título do eixo Y')

df.Coluna.sample(100)   # retorna 100 registros aleatóriamente

# uma única figura com mais de um gráfico
area = plt.figure(figsize=(16, 12))
g1 = area.add_subplot(2, 1, 1)  # 2 linhas, 1 coluna, posição 1
g2 = area.add_subplot(2, 1, 2)  # 2 linhas, 1 coluna, posição 2
g1, g2 = 'criar gráfico 1', 'criar gráfico 2'
area    # imprime o gráfico

# salvar gráficos
area.savefig('grafico.png', dpi = 300, bbox_inches = 'tight')   # bbox_inches para retirar o excesso de borda branca em volta
