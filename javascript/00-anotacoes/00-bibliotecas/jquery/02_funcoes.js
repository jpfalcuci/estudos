// Contar caractéres
var termo = "Aprendendo Javascript";
alert(termo.length);


// Maíusculas e minúsculas
var palavra = "InFORmÁtica";
alert(palavra.toUpperCase());   // Maíusculas
alert(palavra.toLowerCase());   // Minúsculas


// Localizar elementos
var nomes = "João Paulo";
alert(nome.indexOf("o"));       // 1
alert(nome.lastIndexOf("o"));   // 9


// Extrair elementos
var termo = "Aprendendo Javascript";
alert(termo.slice(10));     // "Javascript"
alert(termo.slice(10, 15)); // "Java"


// Arredondar valores
var nota = 7.89;
alert(Math.round(nota));    // 8


// Mínimo e máximo
alert(Math.min(-10, 5, 0, 100, -25, 2));    // -25
alert(Math.max(5, 7, 9, -13, 0, 15));       // 15


// Número aleatório
alert(Math.random());               // Cria números de 0 a 1
var numero = Math.random() * 100    // Cria números de 1 a 100
alert(numero);
alert(Math.round(numero));


// Novas funções
function somar(num1, num2) {
    return num1 + num2;
}
alert(somar(5, 6));
