<?php

// Incluir a conexão com o banco de dados
include("conexao.php");

// Obter dados
$obterDados = file_get_contents('php://input');

// Extrair dados do JSON
$extrair = json_decode($obterDados);

// Separar dados do JSON
$idCurso = $extrair->cursos->idCurso;

// SQL
$sql = "DELETE FROM cursos WHERE idCurso = '$idCurso'";

// Executar a query
$executar = mysqli_query($conexao, $sql);

?>
