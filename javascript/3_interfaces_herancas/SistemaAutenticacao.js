/*
Ser autenticável significa ter o método "autenticar"
*/

export class SistemaAutenticacao {
    static login(autenticavel, senha) {
        if (SistemaAutenticacao.ehAutenticavel(autenticavel)) {
            return autenticavel.autenticar(senha);
        }
        return false;
    }

    static ehAutenticavel(autenticavel) {
        return "autenticar" in autenticavel &&              // verifica se a chave existe dentro do objeto 
            autenticavel.autenticar instanceof Function     // verifica se ele é uma função
    }
}