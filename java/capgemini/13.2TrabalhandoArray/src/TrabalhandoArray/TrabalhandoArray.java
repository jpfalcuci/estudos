package TrabalhandoArray;

import javax.swing.JOptionPane;

public class TrabalhandoArray {
	public static void main(String[] args) {
		//declarando o array
		String [] paises = new String[5];

		// inicializando o array
		paises[0] = "Brasil";
		paises[1] = "Alemanha";
		paises[2] = "Itália";
		paises[3] = "Áustria";
		paises[4] = "Polônia";

		for (String lista: paises) {
			System.out.println(lista);
		}

		// inserindo dados no array
		int [] numeros = new int [10];

		for (int i = 0; i < numeros.length; i++) {
			numeros[i] = Integer.parseInt(JOptionPane.showInputDialog("Informe um número"));
		}

		// listando os valores do array com um ForEach
		System.out.println("Após a entrada de dados");
		for (int listaNumeros : numeros) {
			System.out.print(listaNumeros + " ");
		}

		// calculando os valores para armazenar no array
		numeros[8] = numeros[7] + 4;
		System.out.println("\nApós a alteração do valor na posição 8");

		// listando os valores do array com um ForEach
		for (int listaNumeros : numeros) {
			System.out.print(listaNumeros + " ");
		}
	}
}
