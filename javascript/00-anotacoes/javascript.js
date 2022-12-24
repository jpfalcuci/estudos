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

// DOM => document object model

document                            // é onde o js vai buscar as informações (html)
document.getElementById('id')       // seleciona elementos pelo ID, ByClass e outros
document.querySelector('.class')    // usa a mesma estrutura de seleção do css
console.log('msg')                  // escreve mensagem no console
document.write('string');
document.classList                  // retorna um array com os nomes das classes
document.classList[0]               // retorna uma string com a classe do index [n]
input.value			                // para saber o valor da variável 'input'
input.focus			                // deixa a caixa 'input' em foco
evento.target                       // retorna o alvo da ação
target.textContent                  // retorna o conteúdo do texto
target.parentNode                   // retorna o pai do elemento
button.onclick			            // executa função, chamando sem () ele só imprime a função no console
button.oncontextmenu	            // clique direito, usar 'return false' p/ ñ exibir menu de contexto
evento.shiftKey			            // true ou false se tecla estiver ativa, https://keycode.info
evento.preventDefault()             // previne algum comportamento padrão


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

preload();	        // carrega arquivos antes do início
loadImage();		// exige parametro o caminho e formato da imagem
loadSound();		// exige parametro o caminho e formato do áudio
file.play();		// executa o arquivo de áudio
file.loop();		// executa o arquivo em loop
document.onclick = tocaSom();   // => executa tocaSom
document.onclick = tocaSom;     // => guarda tocaSom dentro de onclick
// navegadores tem política de bloquear códigos que executam mídias antes do usuário interagir com a página

var ano = 2022;             // declara variável
let bloco                   // variável existe apenas no seu escopo
const constante = 'variável que não é alterada'
var array = [0, 1, 2];      // lista
array.length();				// quantidade de elementos do array
array.push();				// adiciona valor p/ array
array.forEach();            // loop para arrays
array.splice()              // remove um item do array

var tela = document.querySelector('canvas'); 	
tela.onmousemove		// captura movimento do mouse
tela.onmousedown		// botão esquerdo pressionado
tela.onmouseup			// botão direito solto

var pincel = tela.getContext('2d');     // cria 'pincel'
pincel.fillStyle = 'grey';              // cor de preenchimento do pincel
pincel.fillRect = (xi, yi, xf, yf);     // preenche retangulo com cor, .fill preenche outras formas
pilcel.clearRect = (xi, yi, xf, yf);    // limpa retangulo
pincel.arc (x, y, raio, inicial, 2 * Math.PI);  // desenha círculo na tela

var x = 'parametro da função'.pageX - tela.offsetLeft;
var y = 'parametro da função'.pageY - tela.offsetTop;   // descontar offset da tela do navegador

const idAudio = `#som_de_${instrumento}`;   // template string, variável dentro da string, usa cráse

const lista = document.getElementById("lista")
lista.appendChild(objeto_js)        // adiciona elemento no html


function funcao() { alert('msg') }  // função nomeada, reaproveitamento de código
addEventListener('event', funcao)   // executa função quando ocorre evento

// exemplo:
const elemento =  document.querySelector('#elemento')
elemento.addEventListener('click', acao)
function acao() { console.log("mensagem") }

// função anônima, executada apenas onde é declarada
elemento.addEventListener('click', function() { console.log("mensagem") })
// arrow function, a partir do ES6 (não permite usar o this):
elemento.addEventListener('click', () => { console.log("mensagem") })

// parâmetros
function ola(nome) { console.log("Olá " + nome) }
elemento.addEventListener('click', (evento) => { console.log(evento) })

// objeto js
var objeto = {propriedade: "valor"}
var pessoa = {nome: "nome", frase: "frase", enviaFrase() {return this.frase;}}
console.log(pessoa.enviaFrase())

// local storage => salva informações no navegador, lê apenas json, string
console.log(localStorage)
localStorage.setItem("propriedade", "valor")
localStorage.propriedade                // retorna "valor"
localStorage.getItem("propriedade")     // retorna "valor"
localStorage.removeItem("propriedade")
localStorage.clear()                    // limpa todo local storage
localStorage.setItem("item", JSON.stringify(item))  // transforma objeto js em string
const itens = JSON.parse(localStorage.getItem("itens")) || [];  // coleta itens do local storage OU cria lista vazia se não houverem itens


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
 

class Classe {
    // atributos e/ou propriedades
    // return dentro de uma função ou class, faz ignorar restante do bloco
    // todo arquivo .js que começa com letra maíscula, representa uma classe
}

let xhr = new XMLHttpRequest();         // xhr.open('GET', url, true);
xhr.onreadystatechange = function() { } // propriedade disparada sempre que a requisição sofre alteração
