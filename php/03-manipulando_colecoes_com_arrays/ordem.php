<?php

$notas = [
    [
        'aluno' => 'Maria',
        'nota' => 10,
    ],
    [
        'aluno' => 'Vinicius',
        'nota' => 6,
    ],
    [
        'aluno' => 'Ana',
        'nota' => 9,
    ],
];

usort($notas, function (array $nota1, array $nota2): int {
    return $nota2['nota'] <=> $nota1['nota'];
});
var_dump($notas);