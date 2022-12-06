# natural language toolkit
# pip install nltk
import nltk
nltk.download('punkt')
nltk.tokenize.word_tokenize()       # separa palavras de pontuação, e retorna em uma lista
nltk.FreqDist('lista de strings')   # calcula a distribuição de frequência das palavras
