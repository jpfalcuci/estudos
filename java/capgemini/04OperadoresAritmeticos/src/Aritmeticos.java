public class Aritmeticos {
	public static void main(String[] args) throws Exception {
		int num1, num2, num3;

		// soma
		num1 = 10;
		num2 = 20;
		num3 = num1 + num2;
		System.out.println("O resultado da soma é: " + num3);
		System.out.println("----------------------------------");

		// subtracao
		num1 = 10;
		num2 = 20;
		num3 = num1 - num2;
		System.out.println("O resultado da subtracao é: " + num3);
		System.out.println("----------------------------------");

		// multiplicacao
		num1 = 10;
		num2 = 20;
		num3 = num1 * num2;
		System.out.println("O resultado da multiplicacao é: " + num3);
		System.out.println("----------------------------------");

		// divisao
		num1 = 20;
		num2 = 2;
		num3 = num1 / num2;
		System.out.println("O resultado da divisao é: " + num3);
		System.out.println("----------------------------------");

		// incrementando (somando de 1 em 1)
		System.out.print("Incrementando (somando de 1 em 1): ");
		num1 = 1;
		while (num1 <= 10) {
			System.out.print(num1 + " ");
			num1++;
		}
		System.out.println("\n----------------------------------");
		
		// decrementando (subtraindo de 1 em 1)
		System.out.print("Decrementando (subtraindo de 1 em 1): ");
		num1 = 10;
		while (num1 > 0) {
			System.out.print(num1 + " ");
			num1--;
		}
	}
}
