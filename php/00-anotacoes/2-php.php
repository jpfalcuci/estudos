<?php

// array
// sequência de informações, normalmente do mesmo tipo
$idadesList = array(21, 23, 19, 25, 30, 41, 18);
$idadesList = [21, 23, 19, 25, 30, 41, 18];         // forma mais usual
$umaIdade = $idadesList[4];     // acessa pelo índice
echo $umaIdade;                 // 30
echo count($idadeList);         // 7

// iterando por um array
for ($i = 0; $i < count($idadeList); $i++) {
	echo $idadeList[$i] . PHP_EOL;
}

$idadesList[] = 20;     // adiciona um novo item ao final do array

// função list
// recebe variáveis e atribui valores de um array, usando os mesmo índices
list($idadeJoao, $idadeMaria, $idadeJose) = $idadesList;
// 21, 23, 19
list($idadeJoao, , $idadeJose) = $idadesList;
// 21, 19


/* 
array associativo
mapa índice que é associado a um valor
índice => valor
o índice só suporta strings ou inteiros, outros tipos serão convertidos
 */

$conta1 = [
	'titular' => 'João',
	'saldo' => 1500
];
echo $conta1['titular'];	// João
echo $conta1['saldo'];		// 1500

$conta2 = [
	'titular' => 'Maria',
	'saldo' => 1000
];

$conta3 = [
	'titular' => 'José',
	'saldo' => 1200
];

$contas = [$conta1, $conta2, $conta3];

for ($i = 0; $i <count($contas); $i++) {
	echo $contas[$i]['titular'] . PHP_EOL;
}       // João / Maria / José

foreach ($contas as $conta) {
	echo $conta['titular'] . PHP_EOL;
}       // João / Maria / José

$contas = [
	123 => ['titular' => 'João',	'saldo' => 1500], 
	456 => ['titular' => 'Maria',	'saldo' => 400], 
	789 => ['titular' => 'José',	'saldo' => 1200]
];

foreach ($contas as $cpf => $conta) {
	echo $cpf . PHP_EOL;
}		// 123 / 456 / 789

// adicionando um novo item
$contas[147] = ['titular' => 'Marcela', 'saldo' => 1800];

foreach ($contas as $cpf => $conta) {
	echo $conta['titular'] . PHP_EOL;
}	// João / Maria / José / Marcela


/* 
funções e subrotinas
subrotinas executam o código
funções executam o código e devolvem um valor
parametros podem receber especificações de tipos dos valores e o tipo do valor a retornar
 */

// function exibeMensagem (string $mensagem) : void     // void é um tipo especial que significa ausência de valor, não retorna nada
function exibeMensagem (string $mensagem)
{
	// echo $mensagem . PHP_EOL;
	echo $mensagem . '<br>';    // quebra de linha do HTML
}

function sacar(array $conta, float $valorASacar) : array
{
	if ($valorASacar > $conta['saldo']) {
		exibeMensagem("Você não pode sacar");
	} else {
		$conta['saldo'] -= $valorASacar;
	}
	return $conta;
}

function depositar(array $conta, float $valorADepositar) : array 
{
	if ($valorADepositar > 0) {
		$conta['saldo'] += $valorADepositar;
	} else {
		exibeMensagem("Depósitos precisam ser positivos");
	}
	return $conta;
}

$contas[123] = sacar($contas[123], 500);    // 1000
$contas[456] = sacar($contas[456], 500);    // você não pode sacar
$contas[789] = depositar($contas[789], 900);

foreach ($contas as $cpf => $conta) {
	// exibeMensagem("$cpf $conta[titular] $conta[saldo]");    // dentro de uma string, arrays associativos podem ser acessados sem aspas 
	exibeMensagem("$cpf {$conta['titular']} {$conta['saldo']}");    // forma complexa, usando chaves para arrays associativos, recomendado 
}

/* 
habilitar extensões php
abrir arquivo php.ini com editor de textos
procurar extension_dir e descomentar a linha referente ao S.O.
procurar o nome da extensão e descomentar a linha
*/

function titularMaiuscula(array &$conta)	// por padrão as funções recebem uma cópia dos valores (passagem por valor)
{											// para que a função receba o endereço do valor, usa-se o "&" (passagem por referência)
											// assim as funções passam a poder alterar toda variável, deve-se usar com cautela
	// $conta['titular'] = strtoupper($conta['titular']);		// função nativa para transformar string em maiuscula
	$conta['titular'] = mb_strtoupper($conta['titular']);	// extensão mbstring, recomendado para utilizar com strings
}


titularMaiuscula($contas['789']);
unset($contas[147]);	// remove variáveis da memória; remove item[i] do array

foreach ($contas as $cpf => $conta) {
    // list('titular' => $titular, 'saldo' => $saldo) = $conta;
    ['titular' => $titular, 'saldo' => $saldo] = $conta;    // outra forma de inciar a list
	exibeMensagem("$cpf $titular $saldo");
}


/*
php na web

todo projeto na web precisa de um servidor
php tras um built-in web server para funcionar na própria máquina:
    php -S localhost:8000               (dentro da pasta)
    acesar no navegador localhost:8000  (por padrão busca um arquivo index.html, index.php)
    localhost:8000/file.php             (inicia o arquivo php)
    ctrl+u abre uma nova aba e mostra o código fonte
*/


function exibeConta(array $conta)
{
    ['titular' => $titular, 'saldo' => $saldo] = $conta;
    echo "<li>Titular: $titular. Saldo: $saldo</li>";
}

echo "<ul>";
foreach ($contas as $cpf => $conta) {
    exibeConta($conta);
}
echo "</ul>";

?> // a partir de agora é tudo texto, pode ser html 

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Contas correntes</h1>

    <dl>
        <?php foreach($contasCorrentes as $cpf => $conta) { ?>
        <dt>
            <h3><?= $conta['titular']; ?> - <?= $cpf; ?></h3>
        </dt>
        <dd>Saldo: <?= $conta['saldo']; ?></dd>
        <?php } ?>
    </dl>
</body>




operações com decimais

pecl install decimal
adicionar no php.ini a linha "extension=decimal"

precisa do pacote libmpdecimal instalado
    linux:    
        sudo apt-get install libmpdec-dev
        edite ou crie o arquivo
            /etc/php/7.2/mods-available/decimal.ini
        coloque as linhas
            ; priority=30
            extension=decimal

<?php

use Decimal\Decimal;

$debitos = array();
$creditos = array();

array_push($debitos, new Decimal("0.1"));
array_push($debitos, new Decimal("0.2"));

array_push($creditos, new Decimal("0.3"));

function saldo(array $creditos, array $debitos) {
    return array_sum($creditos) - array_sum($debitos);
}

echo saldo($creditos, $debitos);    // 0

?>
