php é uma linguagem de programação com diversos propósitos, especialmente desenvolvida para a web
php: hypertext preprocessor (pré-processador de hipertexto)
podemos entendê-lo como uma linguagem de programação (server-side) interpretada, quando alteramos o nosso código, não precisa compilar novamente para que ele seja legível por algum programa ou pela própria máquina, o que traz algumas vantagens e desvantagens (produtividade é a principal vantagem)
o php é melhor aplicado em ambiente web (instalado em servidores e servindo páginas com conteúdo dinâmico), mas também funciona em outros ambientes como iot, linha de comando, aplicativos desktop, entre outros

frameworks para web
    symfony (aplicações entreprise)
    laravel (mais utilizado, produtividade)
    laminas, cakephp, codeigniter, zend framework

instalar php no linux => sudo apt install php
windows => download da versão x64 non thread safe
    editar as variáveis de ambiente do sistema > Variáveis de Ambiente >
    Variável 'Path' > Editar > Novo > Adicionar caminho do php.exe
    
    no terminal:
    php -v      mostra a versão instalada
    php -a      abre o terminal interativo do php
    quit        sai do terminal

echo                para imprimir/exibir na tela
;                   para finalizar uma instrução
$var =              $ para atribuição de variáveis
gettype()           retorna o tipo do objeto informado
'str' . $var        . para concatenar 'string' e $variavel
"string $var"       string com aspas duplas reconhece $variavel
'string'            dentro é tudo string
"string"            string que pode ter variáveis e/ou caractéres especiais

o interpretador php não considera quebras de linha e espaços em branco

<?php // instrução para executar código php

echo "Hello world!\n";  // string

$nome = 'João';     // declarando uma variável
$idade = 29;
echo $idade;        // 29

$idadeDaqui10Anos = $idade + 10;
echo $idadeDaqui10Anos;     // 39

$idadeHa5Anos = $idade - 5;
echo $idadeHa5Anos;         // 24

$soma = 2 + 2;
$subtracao = 2 - 2;
$multiplicacao = 2 * 2;
$divisao = 2 / 2;
$potenciaAoCubo = 2 ** 3;
$restoDaDivisao = 10 % 3;

echo gettype($idade);           // integer

$salario = 1000.5;
echo gettype($salario);         // double (decimal com mais precisão, precisão dupla); float

echo 10 / 3;                    // 3.3333333333333
$true = true; $false = false;   // boolean

echo 'minha idade é ' . $idade . ' anos';   // minha idade é 29 anos
echo "minha idade é $idade anos\n";         // minha idade é 29 anos

/* 
\n  fim de linha
\r  retorno de carro
\t  tab horizontal
\v  tab vertical
\e  escape
\f  form feed
\\  contrabarra ou barra invertida
\$  cifrão
\"  aspas duplas
geralmente a quebra de linhas do windows usa \r\n
*/

echo "linha 1" . PHP_EOL;   // 'end of line' de cada sistema operacional
echo "linha 2";             // linha 1 / linha 2

$numeroDePessoas = 2;

if ($idade >= 18) {
	echo "Você tem $idade anos, autorizado";
} else if ($idade >= 16 && $numeroDePessoas > 1) {
	echo "Você tem $idade anos e está acompanhado, autorizado";
} else {
	echo "Você tem $idade anos, não está autorizado";
}

/* 
operadores lógicos
&&      and
||      or
*/

// operador ternário
$variavel = $condicao ? $valorSeVerdadeiro : $valorSeFalso;

$idade = 15;
$mensagem = $idade < 18 ? 'Você é menor de idade' : 'Você é maior de idade';
echo $mensagem;

// iteração com while (melhor para limites indefinidos)
$contador = 1;
while ($contador <= 15) {
	echo "#$contador" . PHP_EOL;
	$contador += 1;
}

// iteração com for (melhor para limites definidos)
for ($contador = 1; $contador <= 15; $contador++) {
    echo "#$contador" . PHP_EOL;
}

for ($contador = 1; $contador <= 15; $contador++) {
    if ($contador == 13) {
    	continue; // pula a iteração e inicia a próxima
    }
    echo "#$contador" . PHP_EOL;
}

for ($contador = 1; $contador <= 15; $contador++) {
    if ($contador == 13) {
    	break; // sai do loop
    }
    echo "#$contador" . PHP_EOL;
}

// exibir números impares
for ($i = 1; $i < 100; $i++) {
	if ($i % 2 != 0) {
		echo $i . PHP_EOL;
	}
}

// tabuada
$multiplicador = 3;
for ($i = 1; $i <= 10; $i++) {
	$resultado = $multiplicador * $i;
	echo "$multiplicador x $i = $resultado" . PHP_EOL;
}

// imc
$peso = 72;
$altura = 1.76;
$imc = $peso / $altura ** 2;

echo "Seu IMC é de $imc. Você está com o IMC ";
if ($imc < 18.5) {
    echo "abaixo";
} elseif ($imc < 25) {
    echo "dentro";
} else {
    echo "acima";
}
echo " do recomendado";


// switch e match
abstract class Question {}
class Single extends Question {}
class Multiple extends Question {}

// switch
$input = 'single';
switch ($input) {   // usa == (verifica valor?)
    case 'single':
        $question = new Single();
        break;
    case 'multi':
        $question = new Multiple();
        break;
    default:
        throw new Exception(message:'Invalid question type');
}
var_dump($question);    // visualizar um dado, tipo, estrutura e conteúdo; apenas para desenvolvimento

// match
$input = 'single';
$question = match ($input) {    // usa === (verifica valor e tipo)
    'single' => new Single(),
    'multi', 'multiple' => new Multiple()
}; // função anônima precisa de ;
var_dump($question);

// importando outros arquivos
include('file.php');
include 'file.php';     // mais comum
// se não encontra o arquivo, dá um aviso mas continua as execuções

require 'file.php';         // retorna um erro se não encontra o arquivo
require_once 'file.php';    // importa o arquivo apenas se não houver sido importado antes



// operador identico ===

$variavel = 0;

$variavel == 0;     // true
$variavel == null;  // true; na comparação do php, 0 é igual a null

$variavel === 0;    // True
$variavel === null; // false

?>
