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


document.write('string');
console.log                         // exibe resultado no console
alert('cria um popup na tela');
prompt('popup com pergunta');
isNaN('NaN(not a number), retorna true ou false');
document.querySelector('input');	// pega o parâmetro 'input' do html
input.value							// para saber o valor da variável 'input'
input.focus							// deixa a caixa 'input' em foco

button.onclick			// executa função no clique esquerdo, chamando sem () ele só imprime a função no console
button.oncontextmenu	// clique direito, quando não quiser exibir menu de contexto, usar 'return false' na função
evento.shiftKey			// recebe true ou false se tecla estiver ativa, https://keycode.info
tela.onmousemove		// captura movimento do mouse
tela.onmousedown		// botão esquerdo pressionado
tela.onmouseup			// botão direito solto

var ano = 2022;             // variável "ano" recebe "2022", também usa 'let'
const mes = 12		        // declara uma constante
var array = [0, 1, 2];      // lista
array.length();				// retorna a quantidade de elementos do array
array.push();				// empurra parâmetro p/ array

function verbo() {
    //cria uma função com conjunto de instruções dentro do bloco
    return 'valor'
}
// funções anônimas são funções sem nomes criadas dentro de uma variável

Math.round();	// arredonda valor
Math.floor();	// arreonda p/ baixo
Math.random();	// gera número aleatório
Math.PI 		// 3,1415...
parseInt();		// converte string em número (se possível)
parseFloat();	// converte string em número mantendo as casas decimais

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
    // se true, executa código
} else {
    // código se false
}

while(true) {
    // enquanto true, executa código
    break // finaliza loop (cuidado com loop infinito)
}

for (var i = 0; i <= 5; i++) {
    // início, condição de execução, acréscimo
    console.log(i);
 }
 

var tela = document.querySelector('canvas'); 	
var pincel = tela.getContext('2d');			// cria 'pincel'
pincel.fillStyle = 'grey';					// cor de preenchimento do pincel
pincel.fillRect = (xi, yi, xf, yf);			// preenche retangulo com cor, ou .fill preenche outras formas
pilcel.clearRect = (xi, yi, xf, yf);		// limpa retangulo
var x = 'parametro da função'.pageX - tela.offsetLeft;
var y = 'parametro da função'.pageY - tela.offsetTop;   // descontar offset da tela do navegador
pincel.arc (x, y, raio, inicial, 2 * Math.PI);          // desenha círculo na tela

setInterval(função, intervalo);	// recebe função e intervalo em milissegundos

preload();	        // carrega arquivos antes do início
loadImage();		// exige parametro o caminho e formato da imagem
loadSound();		// exige parametro o caminho e formato do áudio
file.play();		// executa o arquivo de áudio
file.loop();		// executa o arquivo em loop

document.querySelector('x');    // buscar elementos do html, padrão CSS (tag .class #id input[type=tel]) 

// navegadores tem política de bloquear códigos que executa mídias antes do usuário interagir com a página
document.onclick = tocaSom();   // => js já tenta executar imediatamente tocaSom
document.onclick = tocaSom;     // => js guarda tocaSom dentro de onclick

const idAudio = `#som_de_${instrumento}`;   // template string, variável dentro da string, usa cráse

document.classList      // retorna um array com os nomes das classes
document.classList[0]   // retorna uma string com a classe do index [n]

class Classe {
    // atributos e/ou propriedades
    // return dentro de uma função ou class, faz ignorar restante do bloco
    // todo arquivo .js que começa com letra maíscula, representa uma classe
}

let xhr = new XMLHttpRequest();         // xhr.open('GET', url, true);
xhr.onreadystatechange = function() { } // propriedade disparada sempre que a requisição sofre alteração
