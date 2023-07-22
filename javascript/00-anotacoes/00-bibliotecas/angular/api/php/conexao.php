<?php

// Variáveis de acesso
$url = "localhost";
$usuario = "root";
$senha = "";
$base = "api";

// Conexão com o banco de dados
$conexao = mysqli_connect($url, $usuario, $senha, $base);

// Arrumar caracteres especiais
mysqli_set_charset($conexao, "utf8");

?>
