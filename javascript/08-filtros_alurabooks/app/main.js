let livros = [];
const endpointDaApi = "https://guilhermeonrails.github.io/casadocodigo/livros.json";

getBuscarLivrosDaAPI();


async function getBuscarLivrosDaAPI() {
    const res = await fetch(endpointDaApi);
    livros = await res.json();
    // console.table(livros);
    let livrosComDesconto = aplicarDesconto(livros);
    exibirOsLivrosNaTela(livrosComDesconto);
}
