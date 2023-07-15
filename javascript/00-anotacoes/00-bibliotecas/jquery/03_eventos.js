// Evento de clique

// <button onclick="mensagem()">Clique aqui</button>

function mensagem() {
    alert("Você clicou no botão");
}


// Evento de mudança, alteração

/* <select onchange="mensagem()" id="cursos">
    <option>Escolhar seu curso</option>
    <option>HTML</option>
    <option>CSS</option>
    <option>Javascript</option>
</select> */

function mensagem() {
    var curso = document.getElementById("cursos").value;
    alert(curso);
}


// Evento de carregamento da página (só funciona na tag body)

// <body onload="mensagem()"></body>

function mensagem() {
    alert("Seja bem vindo ao site");
}


// Eventos de teclado

// onKeyUp: Exibe caractere e depois executa ação
// onKeyDown: Executa ação e depois exibe caractere
// onKeyPress: Executa ação e depois exibe caractere (Não tem suporte as teclas F1-12, Alt, Ctrl, Shift...)

// <input type="text" id="campo" onkeyup="exibir()"></input>
function exibir() {
    var campo = document.getElementById("campo").value;
    alert(campo);
}
