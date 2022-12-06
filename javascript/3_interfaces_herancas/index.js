import { Cliente } from "./cliente.js";
import { Gerente } from "./funcionarios/gerente.js";
import { Diretor } from "./funcionarios/diretor.js";
import { SistemaAutenticacao } from "./SistemaAutenticacao.js";

/* import { ContaCorrente } from "./conta/ContaCorrente.js";
import { ContaPoupanca } from "./conta/ContaPoupanca.js";
import { ContaSalario } from "./conta/ContaSalario.js";

const cliente1 = new Cliente("Ricardo", 11122233309);
const contaCorrenteRicardo = new ContaCorrente(cliente1, 1001);
const contaPoupancaRicardo = new ContaPoupanca(50, cliente1, 1001);
const contaSalarioRicardo = new ContaSalario(cliente1); */

const diretor = new Diretor("Rodrigo", 10000, 12345678900);
diretor.cadastrarSenha("123456");
const gerente = new Gerente("Ricardo", 5000, 12345678901);
gerente.cadastrarSenha("123");

const cliente = new Cliente("Laís", 78945612379, "456");

const gerenteEstaLogado = SistemaAutenticacao.login(diretor, "123456");
const diretorEstaLogado = SistemaAutenticacao.login(gerente, "123");

const clienteEstaLogado = SistemaAutenticacao.login(cliente, "456");

console.log(gerenteEstaLogado, diretorEstaLogado, clienteEstaLogado);