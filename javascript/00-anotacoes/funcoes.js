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


// validação de idade
function validaIdade(data) {
    const dataAtual = new Date();
    const dataMais18 = new Date(data.getUTCFullYear() + 18, data.getUTCMonth(), data.getUTCDate());
    return dataAtual >= dataMais18;
}


// validação de cpf
function validaNumerosRepetidos(cpf) {
    const numerosRepetidos = ['00000000000', '...', '99999999999']
    return numerosRepetidos.includes(cpf);
}

function validaDigito(cpf, mult, tam) {
    let soma = 0;
    let multiplicador = mult;
    for (let tamanho = 0; tamanho < tam; tamanho++) {
        soma += cpf[tamanho] * multiplicador;
        multiplicador--;
    }
    soma = (soma*10) % 11;
    if (soma==10 || soma==1) {
        soma = 0;
    }
    return soma != cpf[tam];
}
