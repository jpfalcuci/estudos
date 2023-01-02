// arrays

var array = [0, 1, 2];      // lista
array.length();				// quantidade de elementos do array
array.push();				// adiciona valor p/ array
array.forEach();            // loop para arrays
array.splice();             // remove um item do array

array.map(livro => {        // executa função para cada item do array
    return {...livro, preco:livro.preco-(livro.preco*desconto)}
}); // ... faz uma cópia de todo objeto para outro, neste caso, alterando o parametro preco

array.filter( i => {        // método para filtrar array, devolve condições True
    return i >= 18;
});

array.sort((a,b)=>a-b);     // ordenar itens do array, necessário passar função de ordenação
array.reduce((acc,atual)=>acc+atual)    // aplica uma função no array e retorna um único valor
array.concat()              // junta dois ou mais arrays em um novo
array.pop()                 // remove o último elemento
array.includes()            // verifica se um elemento está no array
array.fill()                // preenche com elemento especificados
array.indexOf()             // retorna o índice do primeiro elemento encontrado
array.slice(1,3)            // retorna elementos no intervalo de índices indicado
array.some()                // verifica se algum elemento do array passa em um teste (função callback)
array.join()                // une os elementos do array em formato de string
array.shift()
array.unshift()
array.splice()
array.toString()
array.findIndex()
array.find()
array.at()
array.isArray()
array.every()
array.copyWithin()
array.lastIndexOf()
array.valueOf()
array.keys()


// objeto js

var objeto = {propriedade: "valor"}
var pessoa = {nome: "nome", frase: "frase", enviaFrase() {return this.frase;}}
console.log(pessoa.enviaFrase())