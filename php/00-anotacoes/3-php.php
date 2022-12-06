<?php

// criando um array (ou vetor)
$array = array();
$array = [1, 2, 3, 4];

// array associativo
// chave precisa ser inteiro ou string
// booleano e float seriam convertidos
// pesquisar sobre hash map ou hash table
$array = [
	0 => 'zero',
	1 => 'um',
	2 => 'dois'
];


// iterando sobre os valores
foreach ($array as $nome) {
	echo $nome . PHP_EOL;
}	// zero; um; dois

for ($i = 0; $i < count($array); $i++) {
    echo $array[$i] . PHP_EOL;
}	// zero; um; dois


// iterando sobre as chaves e valores
foreach ($array as $numeral => $nome) {
	echo "$numeral em portugês é $nome" . PHP_EOL;
}	// 0 em portugês é zero; 1 em portugês é um; 2 em portugês é dois


// contando itens
$contador = 0;
foreach ($array as $nome) {
	$contador++;
}
echo "Total de itens: $contador" . PHP_EOL;	// Total de itens: 3

// outra forma (melhor)
echo "Total: " .count($array) . PHP_EOL;	// Total: 3
echo "Total: " .sizeof($array) . PHP_EOL;	// Total: 3; menos utilizada


$notas = [ 10, 8, 9, 7];

$notasOrdenadas = $notas;
sort($notasOrdenadas);	// modifica a variável

echo 'Desordenadas:';
var_dump($notas); // Desordenadas: array(4) {[0]=>int(10) [1]=>int(8) [2]=>int(9) [3]=>int(7)}

echo 'Ordenadas:';
var_dump($notasOrdenadas); // Ordenadas: array(4) {[0]=>int(7) [1]=>int(8) [2]=>int(9) [3]=>int(10)}


// definindo critério

$notas = [
	[ 'aluno' => 'Maria', 'nota' => 10],
	[ 'aluno' => 'Vinícius', 'nota' => 6],
	[ 'aluno' => 'Ana', 'nota' => 9]
];

function ordenaNotas(array $nota1, array $nota2): int
{
	if ($nota1['nota'] > $nota2['nota']) {
		return -1; // se o primeiro parâmetro precisar vir antes
	}
	if ($nota2['nota'] > $nota1['nota']) {
		return 1; // se o segundo parâmetro precisar vir antes
	}
	return 0; // se forem iguais
}


// funções anônimas; quando a função só vai ser utilizada para ser passada como parâmetro

// user sort: array a ser ordenado; função que define o critério de ordenação
usort($notas, function (array $nota1, array $nota2): int {
	return $nota1['nota'] <=> $nota2['nota']; 
	// mesma função: se o 1º elemento for menor retorna -1, se for maior retorna 1, se iguais retorna 0
	// nesse caso, retorna a ordem crescente, para a ordem decrescente, inverter os elementos
}); 
var_dump($notas);

// ordem reversa
$notas = [10,8,9,7,6];

// reverse sort
rsort($notas);	// ordena de forma decrescente
var_dump($notas);

// mantendo as chaves
$notas = [
	'Ana' => 10,
	'Roberto' => 7,
	'Maria' => 9,
	'Vinicius' => 6,
	'João' => 8,
];

//associative reverse sort
arsort($notas);	// ordena de forma decrescente manténdo as chaves

//key sort
ksort($notas);	// ordena utilizando as chaves

//key reverse sort
krsort($notas);	// ordena utilizando as chaves, decrescente

//user key sort
uksort($notas, 'ordenaNotasAlt'); // usa função comparadora ordenando pela chave

var_dump($notas);



$notas = [
	'Ana' => 10,
	'João' => null,
	'Maria' => 9,
	'Roberto' => 7,
	'Vinicius' => 6,
];


// verificação de arrays

echo gettype($notas);	// array

if (gettype($notas) === 'array') {
	echo 'É um array';
}

if (is_array($notas)) {
	echo 'É um array';
}

// retorna true se todas as chaves forem numéricas sequenciais, começando do zero
var_dump(array_is_list($notas)); // false


// verifica a existência

foreach ($notas as $aluno => $nota) {
	if ($aluno === 'Vinicius') {
		return true;
	}
}

echo 'Vinicius fez a prova:'.PHP_EOL;
// verifica se a chave existe
var_dump(array_key_exists('Vinicius', $notas));	// true

echo 'João fez a prova:'.PHP_EOL;
// verifica se existe a chave, e se seu valor não é nulo
var_dump(isset($notas['João'])); // false

echo 'Alguém tirou 10?'.PHP_EOL;
// verifica se o valor existe
var_dump(in_array(10, $notas)); // true

echo 'Quem tirou 10?'.PHP_EOL;
// retorna a chave que possui o valor; se não encontrar retorna false
// por padrão, 10 = '10'; pode receber strict:true para verificar valor e tipo (===)
echo array_search(10, $notas); // Ana


// diferença entre arrays

$notasBimestre1 = [ 'Ana' => 10, 'João' => 8, 'Maria' => 9, 'Roberto' => 7, 'Vinicius' => 6, ];
$notasBimestre2 = ['Ana' => 9, 'João' => 6, 'Maria' => 9, 'Roberto' => 7, ];

// ver https://www.php.net/manual/pt_BR/function.array-diff.php

// retorna um novo array contendo todos os elementos do 1º parametro que não estejam nos outros
var_dump(array_diff($notasBimestre1, $notasBimestre2)); // leva em consideração o valor
// array(1) { ["João"]=>int(8) }

var_dump(array_diff_key($notasBimestre1, $notasBimestre2)); // leva em consideração a chave
// array(1) { ["Vinicius"]=>int(6) }

var_dump(array_diff_assoc($notasBimestre1, $notasBimestre2)); // leva em consideração chave e valor, associative
// array(3) { ["Ana"]=>int(10) ["João"]=>int(8) ["Vinicius"]=>int(6) }


$alunosFaltantes = array_diff_key($notasBimestre1, $notasBimestre2);
$nomesAlunos = array_keys($alunosFaltantes); // pega as chaves do array; https://www.php.net/manual/pt_BR/function.array-keys.php
var_dump($nomesAlunos);
// array(1) { [0]=>string(8) "Vinicius" }

$notasAlunos = array_values($alunosFaltantes); // pega os valores do array
var_dump($notasAlunos); // pega os valores do array
// array(1) { [0]=>int(6) }

// combinar arrays (devem ter o mesmo tamanho)
var_dump(array_combine($notasAlunos, $nomesAlunos));
// array(1) { [6]=>string(8) "Vinicius" }

// inverte chaves e valores
var_dump(array_flip($alunosFaltantes));
// array(1) { [6]=>string(8) "Vinicius" }


// unindo arrays

$alunos2021 = [ 'teste'=>'Ana', 'João', 'Maria'];
$novosAlunos = [ 'teste'=>'Roberto', 'Vinicius'];

// combina os dois arrays; não preserva as chaves numéricas (chaves em string são sobrescritas)
$alunos2022 = array_merge($alunos2021, $novosAlunos);
var_dump($alunos2022);
// array(5) { ["teste"]=>string(7) "Roberto" [0]=>string(5) "João" [1]=>string(5) "Maria" [2]=>string(8) "Vinicius" }

// une arrays mas não sobrescreve as chaves
$alunos2022 = $novosAlunos + $alunos2021;
var_dump($alunos2022);
// array(3) { ["teste"]=>string(7) "Roberto" [0]=>string(8) "Vinicius" [1]=>string(5) "Maria" }


// desempacotamento de arrays; traz todos os valores separadamente
// mesma sintaxe do array_merge, porém pode adicionar valores no meio que não são arrays
// ... => operador de unpacking neste contexto
$alunos2022 = [...$alunos2021, 'Lillity', ...$novosAlunos];
var_dump($alunos2022);
// array(5) { ["teste"]=>string(7) "Roberto" [0]=>string(5) "João" [1]=>string(5) "Maria" [2]=>string(7) "Lillity" [3]=>string(8) "Vinicius" }


// adicionar e remover elementos

// recebe array e elementos a serem adicionados
array_push($alunos2022, 'Alice', 'Bob', 'Charlie');
var_dump($alunos2022);
// array(8) { ["teste"]=>string(7) "Roberto" [0]=>string(5) "João" [1]=>string(5) "Maria" [2]=>string(7) "Lillity" [3]=>string(8) "Vinicius" [4]=>string(5) "Alice" [5]=>string(3) "Bob" [6]=> string(7) "Charlie" }

// adicionar único elemento
$alunos2022[] = 'Luiz';
var_dump($alunos2022);
// array(9) { ["teste"]=>string(7) "Roberto" [0]=>string(5) "João" [1]=>string(5) "Maria" [2]=>string(7) "Lillity" [3]=>string(8) "Vinicius" [4]=>string(5) "Alice" [5]=>string(3) "Bob" [6]=> string(7) "Charlie" [7]=>string(4) "Luiz" }

// adicionar elementos no início
array_unshift($alunos2022, 'Stephane');
var_dump($alunos2022);
// array(10) { [0]=>string(8) "Stephane" ["teste"]=>string(7) "Roberto" [1]=>string(5) "João" [2]=>string(5) "Maria" [3]=>string(7) "Lillity" [4]=>string(8) "Vinicius" [5]=>string(5) "Alice" [6]=>string(3) "Bob" [7]=> string(7) "Charlie" [8]=>string(4) "Luiz" }

// remove e retorna primeiro elemento, e reordena índices numéricos 
echo array_shift($alunos2022);
// Stephane

// remove e retorna o último elemento
echo array_pop($alunos2022);
// Luiz


// conjunto de elementos onde a função tem significado (tupla no python)

// função list
$dados = ['Lilly', 10, 19];
list($nome, $nota, $idade) = $dados;

list($nome, $nota, $idade) = $dados; // usa índices numéricos
var_dump($nome, $nota, $idade); // string(5) "Lilly" int(10) int(19)

// usando chaves
$dados = ['nome' => 'Lilly', 'nota' => 10, 'idade' => 19];
['nome'=>$nome, 'nota'=>$nota, 'idade'=>$idade] = $dados; // outra sintaxe da função list
var_dump($nome, $nota, $idade); // string(5) "Lilly" int(10) int(19)

// transformar chaves do array em variáveis
$dados = ['nome' => 'Lilly', 'nota' => 10, 'idade' => 19];
extract($dados); // usar apenas em dados onde se tem total confiança
var_dump($nome, $nota, $idade); // string(5) "Lilly" int(10) int(19)

// criar array utilizando variáveis que existem
var_dump(compact('nome', 'idade', 'nota'));
// array(3) { ["nome"]=>string(5) "Lilly" ["idade"]=>int(19) ["nota"]=>int(10) }


// filter => pega um array e devolve um novo com alguns elementos filtrados
// map => pega um array e mapeia para um novo com valores modificados
// reduce => reduz toda a lista a um único elemento; ex: somar elementos

?>
