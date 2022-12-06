<?php

$dados = [
    'nome' => 'Vinicius',
    'nota' => 10,
    'idade' => 24,
];
// ['nome' => $nome, 'nota' => $nota, 'idade' => $idade] = $dados;

extract($dados);
var_dump($nome, $nota, $idade);

var_dump(compact('nome', 'nota', 'idade'));