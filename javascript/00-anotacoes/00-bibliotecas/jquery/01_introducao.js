// Exibindo uma caixa de mensagem (pop-up)
window.alert("Aprendendo JavaScript");
alert("Aprendendo JavaScript"); // Também funciona sem chamar a biblioteca 'window'


// Variáveis
var nome = "João";
var idade = 30;
var altura = 1.76;
var estuda = true;

// Exibir os conteúdos:
window.alert(nome);
window.alert(idade);
window.alert(altura);
window.alert(estuda);


// Operadores relacionais
window.alert(5 > 4);    // Maior
window.alert(5 < 4);    // Menor
window.alert(5 == 4);   // Igual
window.alert(5 >= 5);   // Maior ou igual
window.alert(8 <= 12);  // Menor ou igual
window.alert(8 != 9);   // Diferente


// Condicional simples
var idade = 19;

if(idade >= 18) {
    alert("Aprovado");
} else {
    alert("Reprovado");
}


// Condicional aninhada
var media = 8.5;

if(media == 10) {
    alert("Parabéns!");
} else if(media >= 9) {
    alert("Ótimo");
} else if(media >= 8) {
    alert("Bom");
} else if(media >= 7) {
    alert("Na média");
} else if(media >= 5) {
    alert("Em exame");
} else {
    alert("Reprovado");
}


// Operadores lógicos
var media = 10;
var faltas = 20;

if((media >= 7) && (faltas <= 15)) {    // E
    alert("Aprovado");
} else {
    alert("Reprovado");
}


var trabalho1 = 8;
var trabalho2 = 5;

if((trabalho1 >= 7) || (trabalho2 >= 7)) {  // OU
    alert("Aprovado");
} else {
    alert("Reprovado");
}


var trabalho = true;

if(!trabalho == true) {     // NÃO (Inverte o valor)
    alert("Você trabalha");
} else {
    alert("Você não trabalha");
}


// Estrutura de escolha
var codigo = 1;

switch(codigo) {
    case 1:
        alert("Pizza");
        break;
    case 2:
        alert("Suco");
        break;
    case 3:
        alert("Macarrão");
        break;
    default:
        alert("Código inválido");
}


// Laços de repetição
var indice = 1;

while(indice <= 3) {
    alert("Oi "+indice);
    indice++;
}

do {
    alert("Oi "+indice);
    indice++;
} while(indice <= 3)

for(var i = 1; i <= 3; i++) {
    alert("Valor do índice: "+indice);
}


// Vetores
var cursos = ["HTML", "CSS", "Javascript"];
alert(cursos[1]);   // "CSS"


// Objetos
var cursos = [
    {nome:"HTML", carga:20, sala:4},
    {nome:"CSS", carga:10, sala:5},
    {nome:"Javascript", carga:15, sala:6}
]

alert(cursos[0].nome);  // "HTML"
alert(cursos[0].nome+" "+cursos[0].carga);  // "HTML 20"
