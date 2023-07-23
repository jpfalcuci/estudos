public class ComandoForEach {
	public static void main(String[] args) {
		// vamos a um exemplo prático
		// eu vou criar um vetor, carregá-lo já inicializado e em seguida vou
		// ler os elementos do vetor usando um For Each

		int[] vetorNumeros = new int[] {1,2,3,4,5,6,7,8,9,10};

		// varrendo o vetor sem uso do For Each
		System.out.println("Varrendo o vetor sem For Each");
		for (int i = 0; i < vetorNumeros.length; i++) {
			System.out.println("Nr : " + vetorNumeros[i]);
		}

		// varrendo o vetor usando o For Each
		System.out.println("Varrendo o vetor usando o For Each");
		for (int obj : vetorNumeros) {
			System.out.println("Nr : " + obj);
		}
	}
}
