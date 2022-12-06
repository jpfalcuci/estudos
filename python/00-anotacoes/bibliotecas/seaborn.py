# módulo seaborn
# biblioteca de visualização estatística de dados baseada no matplotlib
# feito para trabalhar com DF, usando código mais enxuto e de mais alto nível que o matplotlib
# instalar com 'pip install seaborn'
import seaborn as sns
df = 'DataFrame'
sns.distplot(df.coluna)                                     # gera um gráfico estatístico (será removida da biblioteca)
sns.displot(df.coluna, kde=True)                            # gera um gráfico de barras, kde ativa linha
sns.histplot(df.coluna)                                     # gera um gráfico de barras, kde ativa linha
sns.scatterplot(x='c1', y='c2', data=df)                    # gera um gráfico de dispersão
sns.lmplot(x='c1', y='c2', data=df)                         # gera um gráfico de progressão
sns.violinplot(x='c1', y='c2', data=df)                     # gera um gráfico de 'violino'
sns.catplot(x='c1', y='c2', data=df)                        # gera um gráfico categórico
sns.stripplot(x='c1', y='c2', data=df)                      # gera um gráfico categórico
sns.swarmplot(x='c1', y='c2', data=df)                      # gera um gráfico categórico
sns.catplot(x='c1', y='c2', kind='', data=df)               # gera um gráfico categórico, kind pode receber também 'violin', 'box', 'boxen'
sns.relplot(x='c1', y='c2', kind='line', data=df)           # gera um gráfico de linhas
sns.relplot(x='c1', y='c2', hue='var', data=df)             # gera um gráfico separando por cor o valor de 'hue'
sns.relplot(x='c1', y='c2', hue='var', col='var', data=df)  # gera mais de um gráfico separando pelo valor de 'col'

grafico = sns.displot(df.coluna)        # atribui o gráfico a uma variável, que retornará o endereço na memória
grafico.set_title('título')             # adiciona um título a figura
grafico.figure.suptitle('subtítulo')    # adiciona um título superior a figura
grafico.set(xlabel='x', ylabel='y')     # rotula os eixos x e y
grafico.get_figure()                    # exibe a figura armazenada
imagem = grafico.get_figure()           # atribui a função de exibição do gráfico a uma variável
imagem.savefig('imagen.png')            # salva a figura
sns.set_palette('Accent')               # define a paleta de cores
sns.set_style('darkgrid')               # define o estilo

""" guia para estilos de visualização de gráficos
https://urbaninstitute.github.io/graphics-styleguide/ """

# auto correlação
from pandas.plotting import autocorrelation_plot
autocorrelation_plot(df)
""" Autocorrelação	Interpretação
    1	            correlação perfeita positiva
    0,7 a 0,9	    correlação forte
    0,4 a 0,7	    correlação moderada
    0,2 a 0,4	    correlação fraca
    0	            correlação nula
    < 0	            correlação negativa
    -1	            correlação perfeita negativa """
