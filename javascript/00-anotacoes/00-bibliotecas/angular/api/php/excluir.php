<?php

// Incluir a conexão com o banco de dados
include("conexao.php");

// Verificar se o parâmetro 'idCurso' foi passado na URL
if (!isset($_GET['idCurso'])) {
    // Se não houver o parâmetro 'idCurso', retornar uma mensagem de erro em JSON
    echo json_encode(['error' => 'O parâmetro "idCurso" não foi fornecido.']);
    exit; // Encerrar o script
}

// Obter o valor do parâmetro 'idCurso' da URL
$idCurso = $_GET['idCurso'];

// SQL para excluir o curso com o id informado
$sql = "DELETE FROM cursos WHERE idCurso = $idCurso";

// Executar a query de exclusão
$executar = mysqli_query($conexao, $sql);

// Verificar se a consulta SQL foi executada com sucesso
if ($executar) {
    // Retornar uma resposta vazia em formato JSON (ou qualquer mensagem de sucesso)
    echo json_encode([]);
} else {
    // Caso ocorra algum erro na execução da consulta SQL, retornar uma mensagem de erro em JSON
    echo json_encode(['error' => 'Erro ao excluir o curso.']);
}

?>
