<?php

// Incluir a conexão com o banco de dados
include("conexao.php");

// Obter dados
$obterDados = file_get_contents('php://input');

// Extrair dados do JSON
$extrair = json_decode($obterDados);

// Separar dados do JSON
$nomeCurso = $extrair->cursos->nomeCurso;
$valorCursos = $extrair->cursos->valorCurso;

// SQL
$sql = "INSERT INTO cursos (nomeCurso, valorCurso) VALUES ('$nomeCurso', $valorCurso)";

// Executar a query
$executar = mysqli_query($conexao, $sql);

// Exportar os dados cadastrados
$curso = [
    'nomeCurso' => $nomeCurso,
    'valorCurso' => $valorCurso
];

json_encode(['curso' => $curso]);

?>
