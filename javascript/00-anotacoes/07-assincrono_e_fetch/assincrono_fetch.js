/*
    js síncrono e assíncrono
        síncrono é simultâneo, sincronizado
        assíncrono é a comunicação sem sincronia, aguardar por respostas demoradas
    por padrão, js é síncrono, executa uma tarefa após a outra
    podemos fazer um sistema assíncrono, com tarefas em "segundo plano"
*/

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
