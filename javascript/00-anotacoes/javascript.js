/*
    <script> </script> mundo javascript no html
    strings entre "" ou ''
    recomenda-se usar ;  ao final das instruções
    main.js é por convenção o nome do arquivo principal para js
    
    ESLint é uma ferramenta de análise de código estática para identificar padrões problemáticos encontrados no código JavaScript
    JQuery é uma biblioteca js 
    AJAX é o método de requisição em outras URLs, sem necessidade de recarregar página (CEP, viacep.com.br)

    Strict Mode => Modo estrito
    após ativado, erros que anteriormente eram silenciosos, agora dão erro de execução
    para ativar usar "use strict" no começo do arquivo
*/


alert('cria um popup na tela');
prompt('popup com pergunta');
isNaN('not a number');
onclick="alert('msg')"          // executa função na ação do click
alert('msg')                    // cria um popup
setInterval(função, intervalo);	// recebe função e intervalo em milissegundos

Math.round();       // arredonda valor
Math.floor();       // arreonda p/ baixo
Math.random();      // gera número aleatório
Math.PI 		    // 3,1415...
parseInt();		    // converte string em número (se possível)
parseFloat();	    // converte string em número mantendo as casas decimais
nFloat.toFixed(2)   // arredonda um float com 2 casas decimais


var ano = 2022;             // declara variável
let bloco;                  // variável existe apenas no seu escopo
const constante = 'variável que não é alterada';
const frase = `o ano é ${ano}`;     // template strings


/* 
    ;	    caractere especial que significa 'pula uma linha'
    ==	    igual
    !=	    diferente
    &&	    condição E
    ||	    condição OU
    !	    inverter valor, operador lógico NOT
    +=	    x += y ( x = x + y )
    ++      pós incremento, x++ (x = x + 1)
*/

if(10%2==0) {
    // código
} else {
    // código
}

while(true) {
    // código
    break // cuidado com loop infinito
}

for (var i = 0; i <= 5; i++) {
    // início, condição de execução, acréscimo
    console.log(i);
 }


function funcao(parametros) {
    // código da função
    // return para retornar resultado, ignora a execução do restante
}

class Classe {
    // atributos e/ou propriedades
    // return para retornar resultado, ignora a execução do restante
    // todo arquivo .js que começa com letra maíscula, representa uma classe
}
