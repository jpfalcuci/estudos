<?php

// Incluir a conexão com o banco de dados
include("conexao.php");

// Obter dados
$obterDados = file_get_contents('php://input');

// Extrair dados do JSON
$extrair = json_decode($obterDados);

// Separar dados do JSON
$idCurso = $extrair->cursos->idCurso;
$nomeCurso = $extrair->cursos->nomeCurso;
$valorCursos = $extrair->cursos->valorCurso;

// SQL
$sql = "UPDATE cursos SET nomeCurso = '$nomeCurso', valorCurso = $valorCurso WHERE idCurso = $idCurso";

// Executar a query
$executar = mysqli_query($conexao, $sql);

// Exportar os dados alterados
$curso = [
    'idCurso' => $idCurso,
    'nomeCurso' => $nomeCurso,
    'valorCurso' => $valorCurso
];

json_encode(['curso' => $curso]);

?>
