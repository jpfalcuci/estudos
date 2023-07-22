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
$valorCurso = $extrair->cursos->valorCurso;

// SQL
$sql = "UPDATE cursos SET nomeCurso = '$nomeCurso', valorCurso = $valorCurso WHERE idCurso = $idCurso";

// Executar a query
$executar = mysqli_query($conexao, $sql);

// Verificar se a consulta SQL foi executada com sucesso
if ($executar) {
    // Buscar o curso atualizado no banco de dados
    $sql_buscar = "SELECT * FROM cursos WHERE idCurso = $idCurso";
    $executar_buscar = mysqli_query($conexao, $sql_buscar);
    $curso = mysqli_fetch_assoc($executar_buscar);

    // Retornar o curso atualizado em formato JSON
    echo json_encode(['curso' => $curso]);
} else {
    // Caso ocorra algum erro na execução da consulta SQL, retornar uma mensagem de erro em JSON
    echo json_encode(['error' => 'Erro ao atualizar o curso.']);
}

?>
