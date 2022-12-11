import { Cliente } from "./cliente.js";
import { ContaCorrente } from "./ContaCorrente.js";
//no terminal do vscode, usar o comando npm init (node package manager) pra criar o package.json
//o arquivo index tambem tem que ser considerado modulo p o node ler os exports/import
//no arquivo package.json, adicionar o "type": "module"

const cliente1 = new Cliente("Ricardo", 11122233309);
const cliente2 = new Cliente("Alice", 88822233309);

const contaCorrenteRicardo = new ContaCorrente(1001, cliente1);
const contaCorrenteAlice = new ContaCorrente(102, cliente2);

contaCorrenteRicardo.depositar(500);
let valor = 200
contaCorrenteRicardo.transferir(valor, contaCorrenteAlice);

console.log(ContaCorrente.numeroDeContas);