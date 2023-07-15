/* 
<button onClick="acao()">Selecionar</button>

<h1>Proway</h1>
<h1>Seletores JS</h1>
<h1>Curso Proway</h1>
*/

function acao() {
    var texto = document.getElementsByTagName("h1")[0];
    alert(texto.innerHTML);
}


/* 
<button onClick="exibirTexto()">Clique aqui</button>

<h1 class="texto">Título em H1</h1>
<h2 class="texto">Título em H2</h2>
<p class="texto">Parágrafo</p>
*/

function exibirTexto() {
    var campo = document.getElementsByClassName("texto")[2];
    alert(campo.innerHTML);
}


/* 
<input type="text" id="campo">
<button onClick="exibirConteudo()">Clique aqui</button>
*/

function exibirConteudo() {
    var campo = document.getElementById("campo");
    alert(campo.value);
    campo.value = "";
}


/* 
<h1>JavaScript</h1>
<button onClick="acao()">Clique aqui</button>
*/

function acao() {
    var texto = document.getElementsByTagName("h1")[0];
    texto.style.color = "#FF0000";
    texto.style.fontSize = "20px";
    texto.innerHTML = "Curso de JavaScript"
}


/* 
<a href="https://www.link.com.br">Clique aqui</a>
<button onClick="alterarLink()">Alterar link</button>
*/

function alterarLink() {
    var link = document.getElementsByTagName("a")[0];
    link.href = "https://www.outrolink.com.br"
}
