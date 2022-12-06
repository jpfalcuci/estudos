// {/* <script> </script> mundo javascript
// todo texto em javascript entre "" ou ''
// recomenda-se usar ;  ao final das instruções
// /* ignora código */

// document.write('este conteúdo é uma string');
// // concatenação é a "soma" de strings e/ou números

// console.log // exibe resultado no console (F12 ou Ctrl+Shift+J)

// alert('cria um popup na tela');
// prompt('popup com pergunta');
// isNaN('p/ saber se um valor é NaN(not a number), recebe true ou false');

// document.querySelector('input');	// pega o parâmetro 'input' do html
// input.value							// para saber o valor da variável 'input'
// input.focus							// deixa a caixa 'input' em foco

// button.onclick			// executa função no clique esquerdo, chamando sem () ele só imprime a função no console
// button.oncontextmenu	// clique direito, quando não quiser exibir menu de contexto, usar 'return false' na função
// evento.shiftKey			// recebe true se tecla estiver apertada, ou false se não
// tela.onmousemove		// captura movimento do mouse
// tela.onmousedown		// botão esquerdo pressionado
// tela.onmouseup			// botão direito solto

// // teclas		esquerda = 37, cima = 38, direita = 39, baixo = 40,
// https://keycode.info 	para saber códigos das teclas

// var ano = 2022;
// // variável "ano" recebe "2022", também usa 'let'

// const nome					// declara uma constante

// var array = [0, 1, 2];		// lista, mais de um parâmetro, usar variável no plural, primeira posição é '0'
// array.length();				// retorna a quantidade de elementos do array
// array.push();				// empurra parâmetro p/ array

// function verbo() {
//     //cria uma função com conjunto de instruções dentro do bloco
//     return 'valor' // devolve valor p/ função
// }

// funções anônimas são funções sem nomes criadas dentro de uma variável

// Math.round();	// arredonda valor
// Math.floor();	// arreonda p/ baixo
// Math.random();	// gera número aleatório
// Math.PI 		// 3,1415...
// parseInt();		// converte string em número (se possível)
// parseFloat();	// converte string em número mantendo as casas decimais

// ;	// caractere especial que significa 'pula uma linha'
// ==	// igual
// !=	// diferente
// &&	// condição E
// ||	// condição OU
// !	// inverter valor, operador lógico NOT
// +=	// x += y ( x = x + y )
// ++ // pós incremento, x++ (x = x + 1)

// if() {
//     // condição SE, executa instruções dentro de bloco
//     // espera receber true ou false por padrão
// } else {
//     // se o anterior não for verdadeiro
// }

// while() {
//     // enquanto X for verdadeiro, executa instruções dentro do bloco
//     // cuidado com loop infinito
// }

// for(variavel; condição de repetição; intervalo de repetição) {
//     // instrução de repetição
// }

// break // finaliza loop, while/for

// var tela = document.querySelector('canvas'); 	
// var pincel = tela.getContext('2d');			// cria 'pincel'
// pincel.fillStyle = 'grey';					// cor de preenchimento do pincel
// pincel.fillRect = (xi, yi, xf, yf);			// preenche retangulo com cor, ou .fill preenche outras formas
// pilcel.clearRect = (xi, yi, xf, yf);		// limpa retangulo
// var x = 'parametro da função'.pageX - tela.offsetLeft;
// var y = 'parametro da função'.pageY - tela.offsetTop; // descontar offset da tela do navegador
// pincel.arc (x, y, raio, inicial, 2 * Math.PI); // desenha círculo na tela

// setInterval(função, intervalo);	// recebe função e intervalo em milissegundos

// function preload	// carrega arquivos antes do início
// loadImage();		// exige parametro o caminho e formato da imagem
// loadSound();		// exige parametro o caminho e formato do áudio
// file.play();		// executa o arquivo de áudio
// file.loop();		// executa o arquivo em loop

// main.js é por convenção, o nome do arquivo principal para javascript
// document.querySelector('x'); para buscar elementos do html, padrão CSS
// x = tag, .class,  #id, input[type=tel], 

// navegadores tem política de bloquear códigos que executa mídias antes do usuário interagir com a página
// .onclick = tocaSom(); 	=> js já tenta executar imediatamente tocaSom
// .onclick = tocaSom;		=> js guarda tocaSom dentro de onclick

// const idAudio = `#som_de_${instrumento}`;	template string, variável dentro da string, usa cráse
// .classList[0] 	=> lista de classes

// class "Nome"{atributos ou propriedades}
// return dentro de uma função ou class, faz ignorar restante do bloco
// todo arquivo .js que começa com letra maíscula, representa uma classe

// ESLint é uma ferramenta de análise de código estática para identificar padrões problemáticos encontrados no código JavaScript; instalei no terminando usando npx eslint --init
// JQuery é uma biblioteca js 
// AJAX é o método de requisição em outras URLs, sem necessidade de recarregar página (CEP, viacep.com.br)
//     let xhr = new XMLHttpRequest();			xhr.open('GET', url, true);
//     xhr.onreadystatechange = function() { }		// propriedade disparada sempre que a requisição sofre alteração */}