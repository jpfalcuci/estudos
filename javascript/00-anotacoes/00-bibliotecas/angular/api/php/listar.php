<?php

// Incluir a conexão com o banco de dados
include("conexao.php");

// SQL
$sql = "SELECT * FROM cursos";

// Executar a query
$executar = mysqli_query($conexao, $sql);

// Vetor
$cursos = [];

// Índice
$indice = 0;

// Loop
while($linha = mysqli_fetch_assoc($executar)) {
    $cursos[$indice]['idCurso'] = $linha['idCurso'];
    $cursos[$indice]['nomeCurso'] = $linha['nomeCurso'];
    $cursos[$indice]['valorCurso'] = $linha['valorCurso'];
    $indice++;
}

// Retornar o vetor em JSON
json_encode(['cursos' => $cursos]);
// var_dump($cursos);

?>

<!-- http://localhost/api/php/listar.php -->
