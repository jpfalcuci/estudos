// código dos carros

let xCarros = [600, 600, 600, 600, 600, 600];
let yCarros = [40, 96, 150, 210, 270, 318];
let comprimentoCarro = 50;
let alturaCarro = 40;
let velocidadeCarros = [2, 2.5, 3.2, 5, 3.3, 2.3];
let posicaoInicialCarros = 600;
let posicaoFinalCarros = -50;


function mostraCarro() {
  for (let i = 0; i < imagemCarros.length; i++) {
    image(imagemCarros[i], xCarros[i], yCarros[i], comprimentoCarro, alturaCarro);
  }
}

function movimentaCarro() {
  for (let i = 0; i < imagemCarros.length; i++) {
    xCarros[i] -= velocidadeCarros[i];
  }
}

function voltaPosicaoInicialCarro() {
  for (let i = 0; i < imagemCarros.length; i++) {
    if (passouTodaTela (xCarros[i]) ) {
      xCarros[i] = posicaoInicialCarros;
    }
  }
}

function passouTodaTela(xCarros) {
  return (xCarros < posicaoFinalCarros)
}