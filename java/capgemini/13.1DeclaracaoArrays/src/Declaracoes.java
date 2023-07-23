public class Declaracoes {
	public static void main(String[] args) {
		// [ ] - são inseridos em uma variável que referecia um array
		int[] numeros = new int [4];

		// OUTRA MANEIRA DE FAZER UMA DECLARAÇÃO DE ARRAY
		int[] numeros2;
		numeros2 = new int[10];

		// DECLARANDO VÁRIOS ARRAYS
		int[] numeros3 = new int[44], numeros4 = new int[23];

		// { } - inicializar valores em um array sua declaração
		int[] iniciaValores = {12,32,54,6,8,89,64,64,6};

		// DECLARA UM ARRAY DE INTEIROS
		int[] meuArray;

		// ALOCA MEMÓRIA PARA 10 INTEIROS
		meuArray = new int[10];

		// INICIALIZA O PRIMEIRO ELEMENTO
		meuArray[0] = 100;
		meuArray[1] = 85;
		meuArray[2] = 88;
		meuArray[3] = 93;
		meuArray[4] = 123;
		meuArray[5] = 952;
		meuArray[6] = 344;
		meuArray[7] = 233;
		meuArray[8] = 622;
		meuArray[9] = 8522;
		// meuArray [10] = 564; // ESTOURA A PILHA POIS NÃO EXISTE O ÍNDICE 10

		System.out.println(meuArray[9]);
		System.out.println(meuArray[2]);
	}
}
