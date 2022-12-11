import { Cliente } from "./cliente.js";

export class ContaCorrente {
    
    static numeroDeContas = 0;
    agencia;
    _cliente;
    _saldo = 0; // boa prática para propriedade privada, não se deve editar fora do código
    // existe discussão na comunidade para implementação de # antes da propriedade para tornar privada
    // https://github.com/tc39/proposal-class-fields#private-fields


    set cliente(novoValor){
        if (novoValor instanceof Cliente){
            this._cliente = novoValor;
        }
    }

    get cliente(){
        return this._cliente;
    }

    get saldo(){
        return this._saldo;
    }

    constructor(agencia, cliente){
        this.agencia = agencia;
        this.cliente = cliente;
        ContaCorrente.numeroDeContas++;
    }

    sacar(valor) {
        if (this._saldo >= valor) {
            this._saldo -= valor;
            return valor;
        }
    }

    depositar(valor) {
        if (valor <= 0) {
            return; // técnica de early return
        }
        this._saldo += valor;
    }

    transferir(valor, conta){
        const valorSacado = this.sacar(valor);
        conta.depositar(valorSacado);
    }
}