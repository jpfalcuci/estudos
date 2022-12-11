/* 
    regex => padrão, forma de definir determinada cadeia de caracteres dentro de um texto maior

    quantifier: quantas vezes um caractere deve aparecer;
        ? - zero ou uma vez
        * - zero ou mais vezes
        + - uma ou mais vezes
        {n} - exatamente n vezes
        {n,} - no mínimo n vezes
        {n,m} - no mínimo n vezes, no máximo m vezes

    [] => classes de caracteres; dentro não existem meta-char (existem exceções);
        [0-9] significa de 0 até 9
        [A-Z] significa de A até Z, sempre maiúscula
        [a-z] significa de a até z, sempre minúscula
        [A-Za-z] significa A-Z ou a-z
        [abc] significa a, b ou c

    \s => whitespace, normalmente é um atalho para [ \t\r\n\f]
        O primeiro caractere é um espaço branco
        \t é um tab
        \r é carriage return
        \n é newline
        \f é form feed

    \d => todos os dígitos [0-9]
    \w => wordchar [A-Za-z0-9_]

    âncora é uma forma de encontrar uma posição dentro do texto
    \b => word boundary (limites de palavras), \balvo\b
    \B => non-word-boundary
    ^\d => nada deve vir antes do dígito
    \d$ => nada deve vir após o dígito

    ( ) => separar grupos dentro de uma regex, é retornado separado
    ( )? => grupo opcional
    (?: ) => não retornar o grupo

    +? => por padrão, o + vai até o último elemento possível, usando o ? ele para no primeiro elemento encontrado
    
    | => pipe "ou"
    (h1|h2) => dentro de grupos funciona com a expressão toda, h1 ou h2
    (a|b) ... \1 => faz referência ao resultado do grupo 1 (0 é o resultado principal)
*/

var cpf = "\d{3}\.?\d{3}\.?\d{3}[-.]?\d{2}";

// dica para melhor legibilidade:
var DIA  = "[1-3]?\d";
var _DE_ = "\s+de\s+";
var MES  = "[A-ZÇa-zç]{4,9}";
var ANO  = "[12]\d{3}";
var stringRegex = DIA + _DE_ +  MES + _DE_ + ANO;
var objetoRegex  = new RegExp(stringRegex, 'g');

var data = "^Data:[\s]?[0-9]{2}\/[0-9]{2}\/[0-9]{4}$"

/* 
    https://regexr.com/
    https://regex101.com/
*/