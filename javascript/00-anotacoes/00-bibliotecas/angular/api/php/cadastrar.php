<?php

// Incluir a conexão com o banco de dados
include("conexao.php");

// Obter dados
$obterDados = file_get_contents('php://input');

// Extrair dados do JSON
$extrair = json_decode($obterDados);

// Separar dados do JSON
$nomeCurso = $extrair->cursos->nomeCurso;
$valorCurso = $extrair->cursos->valorCurso;

// SQL
$sql = "INSERT INTO cursos (nomeCurso, valorCurso) VALUES ('$nomeCurso', $valorCurso)";

// Executar a query
$executar = mysqli_query($conexao, $sql);

// Verificar se a consulta SQL foi executada com sucesso
if ($executar) {
    $idCurso = mysqli_insert_id($conexao); // Obtém o ID do curso inserido
    $curso = [
        'idCurso' => $idCurso,
        'nomeCurso' => $nomeCurso,
        'valorCurso' => $valorCurso
    ];
    echo json_encode(['curso' => $curso]);
} else {
    // Caso ocorra algum erro na execução da consulta SQL, retornar uma mensagem de erro em JSON
    echo json_encode(['error' => 'Erro ao cadastrar o curso.']);
}

?>
