<?php

$array = [
    0 => 'um',
    1 => 'dois',
    3 => 'tres',
];

foreach ($array as $numeral => $nomeNumero) {
    echo "$numeral em português é: $nomeNumero" . PHP_EOL;
}

echo "Total: " . count($array) . PHP_EOL;

var_dump(array_is_list($array));