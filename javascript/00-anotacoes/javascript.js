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

    js síncrono e assíncrono
        síncrono é simultâneo, sincronizado
        assíncrono é a comunicação sem sincronia, aguardar por respostas demoradas
    por padrão, js é síncrono, executa uma tarefa após a outra
    podemos fazer um sistema assíncrono, com tarefas em "segundo plano"

*/

// DOM => document object model

document                            // é onde o js vai buscar as informações (html)
document.getElementById('id')       // seleciona elementos pelo ID, ByClass e outros
document.querySelector('.class')    // usa a mesma estrutura de seleção do css
console.log('msg')                  // escreve mensagem no console
console.table(lista)                // exibe o conteúdo em formato de tabela
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
nFloat.toFixed(2)   // arredonda um float com 2 casas decimais

preload();	        // carrega arquivos antes do início
loadImage();		// exige parametro o caminho e formato da imagem
loadSound();		// exige parametro o caminho e formato do áudio
file.play();		// executa o arquivo de áudio
file.loop();		// executa o arquivo em loop
document.onclick = tocaSom();   // => executa tocaSom
document.onclick = tocaSom;     // => guarda tocaSom dentro de onclick
// navegadores tem política de bloquear códigos que executam mídias antes do usuário interagir com a página

var ano = 2022;             // declara variável
let bloco;                  // variável existe apenas no seu escopo
const constante = 'variável que não é alterada';
const frase = `o ano é ${ano}`;     // template strings

var array = [0, 1, 2];      // lista
array.length();				// quantidade de elementos do array
array.push();				// adiciona valor p/ array
array.forEach();            // loop para arrays
array.splice();             // remove um item do array
array.map(livro => {        // executa função para cada item do array
    return {...livro, preco:livro.preco-(livro.preco*desconto)}
}); // ... faz uma cópia de todo objeto para outro, neste caso, alterando o parametro preco
array.filter( i => {        // método para filtrar array, devolve condições True
    return i >= 18;
});
array.sort((a,b)=>a-b);     // ordenar itens do array, necessário passar função de ordenação
array.reduce((acc,atual)=>acc+atual)    // aplica uma função no array e retorna um único valor
array.concat()              // junta dois ou mais arrays em um novo
array.pop()                 // remove o último elemento
array.includes()            // verifica se um elemento está no array
array.fill()                // preenche com elemento especificados
array.indexOf()             // retorna o índice do primeiro elemento encontrado
array.slice(1,3)            // retorna elementos no intervalo de índices indicado
array.some()                // verifica se algum elemento do array passa em um teste (função callback)
array.join()                // une os elementos do array em formato de string
array.shift()
array.unshift()
array.splice()
array.toString()
array.findIndex()
array.find()
array.at()
array.isArray()
array.every()
array.copyWithin()
array.lastIndexOf()
array.valueOf()
array.keys()


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


// fetch
// método assíncrono que tem como parâmetro obrigatório a url de uma api
var consultaCEP = fetch('viacep.com.br/ws/01001000/json');
// retorna uma promisse => pode ser retornada "resolvida" ou "rejeitada" em um objeto do tipo response
// para acessar o objeto é necessário converter:
// método .then => "então", faz algo com a resposta recebida, apenas se a promisse tiver sido resolvida
// método .catch => se a promessa for rejeitada
// método .finally => executado nos dois casos, independente da resposta
var consultaCEP = fetch('https://viacep.com.br/ws/0100100/json').then(resposta  => resposta.json())
    .then(r => console.log(r)).catch(erro => console.log(erro))
    .finally(mensagem => console.log("Processamento concluído!"));

// callback hell => situações que geram respostas atrás de respostas, .then após .then
// uma solução é o async await, que faz a função aguardar até ter a resposta
async function buscaEndereco(cep) {
    try {
        var consultaCEP = await fetch(`https://viacep.com.br/ws/${cep}/json`);
        var consultaCEPConvertida = await consultaCEP.json();
        if (consultaCEPConvertida.erro) {
            throw Error("CEP não existente!");
        }
        console.log(consultaCEPConvertida);
        return consultaCEPConvertida;
    } catch(erro) {
        console.log(erro);
    }
}

// várias requisições com Promise
let ceps = ["01001000","01001001"];
let conjuntoCEPs = ceps.map(valores => buscaEndereco(valores));
Promise.all(conjuntoCEPs).then(respostas => console.log(respostas));


/*
nodejs => instalar json-server

    node package manager
        repositório de projetos feitos em node, open-source
        também permite a instalação de bibliotecas e pacotes via linha de comando

    $ npm init
    $ npm install -g json-server
    $ json-server --watch db.json
*/

// quando se usa export de funções, é necessário importar o módulo no html com a tag type="module"
// na primeira linha do arquivo, é feita a importação:
import { nomeDaArquivo } from "./arquivo.js";
import nomeDaFuncao from "./arquivo.js";

function constroiCard(descricao) {
    const video = document.createElement('li');
    video.className = "class__name";
    video.innerHTML = `<p>${descricao}</p>`
}

const listaDeVideos = document.querySelector("[data-lista]");
while (listaDeVideos.firstChild) { 
    listaDeVideos.removeChild(listaDeVideos.firstChild);
} // seleciona os itens do html e apaga todos, útil para adicionar novos itens, como numa busca ou filtro