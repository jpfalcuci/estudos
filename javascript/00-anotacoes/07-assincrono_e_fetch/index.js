const apiUrl = 'http://localhost:5000/clientes'
// const clientes = [{nome: 'teste', cpf: '00000000000'}]
const listaClientes = document.querySelector('#clientes')

/* fetch(apiUrl)
    .then(dados => dados.json)
    .then(resposta => {
        resposta.forEach(cliente => clientes.push({
        nome: cliente.nome,
        cpf: cliente.cpf
    })
    )
    console.log(clientes)
}) */

/* clientes.forEach(cliente =>
    listaClientes.innerHTML += (`<li>nome: ${cliente.nome} cpf: ${cliente.cpf}</li>`)
) */

fetch(apiUrl)
    .then(dados => dados.json)
    .then(resposta => {
        resposta.forEach(cliente => listaClientes.innerHTML += (`<li>nome: ${cliente.nome} cpf: ${cliente.cpf}</li>`))
    })
    .catch(resposta => listaClientes.innerHTML = "<p>erro</p>")
