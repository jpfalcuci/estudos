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
console.log(campo.validity)         // returna uma lista de erros de um campo de input

preload();	        // carrega arquivos antes do início
loadImage();		// exige parametro o caminho e formato da imagem
loadSound();		// exige parametro o caminho e formato do áudio
file.play();		// executa o arquivo de áudio
file.loop();		// executa o arquivo em loop
document.onclick = tocaSom();   // => executa tocaSom
document.onclick = tocaSom;     // => guarda tocaSom dentro de onclick
// navegadores tem política de bloquear códigos que executam mídias antes do usuário interagir com a página

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
addEventListener('blur', funcao)    // blur = quando tira o foco do campo de input

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


// local storage => salva informações no navegador, lê apenas json, string
console.log(localStorage)
localStorage.setItem("propriedade", "valor")
localStorage.propriedade                // retorna "valor"
localStorage.getItem("propriedade")     // retorna "valor"
localStorage.removeItem("propriedade")
localStorage.clear()                    // limpa todo local storage
localStorage.setItem("item", JSON.stringify(item))  // transforma objeto js em string
const itens = JSON.parse(localStorage.getItem("itens")) || [];  // coleta itens do local storage OU cria lista vazia se não houverem itens

let xhr = new XMLHttpRequest();         // xhr.open('GET', url, true);
xhr.onreadystatechange = function() { } // propriedade disparada sempre que a requisição sofre alteração
