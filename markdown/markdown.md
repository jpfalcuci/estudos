# Guia de Uso do Markdown

O Markdown é uma linguagem de marcação leve que permite a formatação de textos de maneira simples e rápida, sendo amplamente utilizada para criar documentos, posts em blogs, documentação e muito mais. Neste guia, você aprenderá os fundamentos do Markdown e como usá-lo para criar documentos bem formatados.

---

## Índice

1. [Introdução ao Markdown](#1-introdução-ao-markdown)
2. [Formatação de Texto](#2-formatação-de-texto)
   - 2.1 [Títulos](#21-títulos)
   - 2.2 [Negrito e Itálico](#22-negrito-e-itálico)
   - 2.3 [Links](#23-links)
   - 2.4 [Listas](#24-listas)
   - 2.5 [Listas de Tarefas](#25-listas-de-tarefas)
   - 2.6 [Tachado](#26-tachado)
   - 2.7 [Fórmulas Matemáticas](#27-formulas-matematicas)
     - 2.7.1 [Equações em Linha](#271-equacoes-em-linha)
     - 2.7.2 [Equações em Bloco](#272-equacoes-em-bloco)
3. [Inserção de Mídia](#3-inserção-de-mídia)
   - 3.1 [Imagens](#31-imagens)
   - 3.2 [Vídeos](#32-vídeos)
4. [Citações](#4-citações)
5. [Linhas Horizontais](#5-linhas-horizontais)
6. [Código Embutido](#6-código-embutido)
7. [Blocos de Código](#7-blocos-de-código)
8. [Tabelas](#8-tabelas)
9. [Notas de Rodapé](#9-notas-de-rodape)
10. [Referências](#10-referências)

---

## 1. Introdução ao Markdown

O Markdown foi desenvolvido para ser uma linguagem de marcação de fácil leitura e escrita, semelhante à escrita em texto simples. Ele é convertido para HTML e outros formatos de saída, tornando-o ideal para criação de conteúdo na web. O Markdown é amplamente utilizado em plataformas como GitHub, Stack Overflow e muitos outros.

## 2. Formatação de Texto

### 2.1 Títulos

Use "#" seguido do texto para criar títulos. O número de "#" indica o nível do título (de 1 a 6).

Exemplo:

```markdown
# Título de Nível 1
## Título de Nível 2
### Título de Nível 3
```

### 2.2 Negrito e Itálico

- Use "\*\*texto\*\*" ou "\_\_texto\_\_" para negrito.
- Use "\*"texto"\*" ou "\_texto\_" para itálico.

Exemplo:

```markdown
**Negrito** ou __Negrito__
*Itálico* ou _Itálico_
```

**Negrito**, _Itálico_

### 2.3 Links

Crie links usando "[texto](URL)".

Exemplo:

```markdown
[Google](https://www.google.com)
```

[Google](https://www.google.com)

### 2.4 Listas

Crie listas ordenadas usando números seguidos de ponto.

Exemplo:

```markdown
1. Item 1
2. Item 2
3. Item 3
```

Crie listas não ordenadas usando "*" ou "-".

Exemplo:

```markdown
- Item A
- Item B
- Item C
```

### 2.5 Listas de Tarefas

Crie listas de tarefas utilizando colchetes e espaços.

Exemplo:

```markdown
- [X] Tarefa concluída
- [ ] Tarefa pendente
```

- [X] Tarefa concluída
- [ ] Tarefa pendente

### 2.6 Tachado

Para adicionar texto tachado (riscado), use dois til (~) antes e depois do texto.

Exemplo:

```markdown
Este texto está ~~tachado~~.
```

Este texto está ~~tachado~~.

### 2.7 Fórmulas Matemáticas

Além das formatações básicas de texto, o Markdown também permite a inserção de fórmulas matemáticas em seus documentos usando a notação do LaTeX.

#### 2.7.1 Equações em Linha

Para incluir fórmulas matemáticas em linha, utilize a sintaxe com cifrões ($).

Exemplo:

```markdown
$ax^2 + bx + c = 0$, onde $a$, $b$ e $c$ são os coeficientes da equação quadrática.
```

$ax^2 + bx + c = 0$, onde $a$, $b$ e $c$ são os coeficientes da equação quadrática.

#### 2.7.2 Equações em Bloco

Se você precisa de uma fórmula matemática mais complexa, é possível utilizar a sintaxe de bloco ($$).

Exemplo:

```markdown
$$
\int_{a}^{b} f(x) \, dx = F(b) - F(a)
$$
```

$$
\int_{a}^{b} f(x) \, dx = F(b) - F(a)
$$

---

## 3. Inserção de Mídia

### 3.1 Imagens

Inclua imagens usando "![texto alternativo](URL da imagem)".

Exemplo:

```markdown
![Computer](https://raw.githubusercontent.com/jpfalcuci/jpfalcuci/main/computer-illustration.png)
```

![Computer](https://raw.githubusercontent.com/jpfalcuci/jpfalcuci/main/computer-illustration.png)

### 3.2 Vídeos

Você pode incorporar vídeos de plataformas como o YouTube.

Exemplo:

```markdown
<iframe width="560" height="315" src="https://www.youtube.com/embed/4_tiv9v964k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/4_tiv9v964k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

## 4. Citações

Use ">" antes do texto para criar citações.

Exemplo:

```markdown
> Isso é uma citação de primeiro nível.
>> Isso é uma citação de segundo nível.
```

> Isso é uma citação de primeiro nível.
>> Isso é uma citação de segundo nível.

---

## 5. Linhas Horizontais

Use três hífens "---" ou três asteriscos "***" para criar linhas horizontais.

Exemplo:

```markdown
---
***
```

---

## 6. Código Embutido

Use "\`código\`" para realçar código inline.

Exemplo:

```markdown
O comando `git clone` é usado para clonar um repositório.
```

O comando `git clone` é usado para clonar um repositório.

---

## 7. Blocos de Código

Use "```" antes e depois do bloco de código para realçar blocos de código. É possível especificar a linguagem de programação para obter realce de sintaxe apropriado.

Exemplo:

\```python
def hello():
    print("Olá, mundo!")
\```

```python
def hello():
    print("Olá, mundo!")
```

---

## 8. Tabelas

Crie tabelas usando hifens para os cabeçalhos e pipes "|" para separar colunas.

Exemplo:

```markdown
| Cabeçalho 1 | Cabeçalho 2 |
|-------------|-------------|
| Dado 1      | Dado 2      |
| Dado 3      | Dado 4      |
```

| Cabeçalho 1 | Cabeçalho 2 |
| ------------ | ------------ |
| Dado 1       | Dado 2       |
| Dado 3       | Dado 4       |

---

## 9. Notas de Rodapé

É possível adicionar notas de rodapé em seu documento usando o formato `[^1]`, onde o número corresponde à nota de rodapé. No final do documento, adicione as notas de rodapé correspondentes, como mostrado abaixo.

Exemplo:

```markdown
Este é um exemplo de texto com uma nota de rodapé.[^1]
[^1]: Esta é a nota de rodapé número 1. Ela contém informações adicionais relacionadas ao texto.
```

Este é um exemplo de texto com uma nota de rodapé.[^1]

[^1]: Esta é a nota de rodapé número 1. Ela contém informações adicionais relacionadas ao texto.

---

## 10. Referências

- [Página Oficial do Markdown](https://daringfireball.net/projects/markdown/)
- [Sintaxe Básica do Markdown](https://www.markdownguide.org/basic-syntax/)
- [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/)

---
