public class RelacionaisLogicos {
	public static void main(String[] args) throws Exception {
		// Operadores Relacionais
		// > < <= >= !=  ==

		int num1, num2;

		// testando uma igualdade
		num1 = 10;
		num2 = 10;
		if (num1 == num2) {
			System.out.println("número 1 e número são iguais");
		}

		// testando uma desigualdade
		num1 = 10;
		num2 = 30;
		if (num1 != num2) {
			System.out.println("número 1 e número são diferentes");
		}

		// testando maior
		num1 = 10;
		num2 = 5;
		if (num1 > num2) {
			System.out.println("número 1 é maior que número 2");
		} else {
			System.out.println("número 2 é maior que número 1");
		}

		// operadores lógicos
		// && = e / AND  || = ou / OR
		num1 = 10;
		num2 = 5;
		int num3 = 20, num4 = 5;
		if ((num1 > num3) && (num2 == num4)) {
			System.out.println("Primeira opção satisfeita");
		} else {
			System.out.println("Segunda opção satisfeita");
		}

		num2 = 10;
		if ((num1 > num3) || (num2 == num4)) {
			System.out.println("Primeira opção satisfeita");
		} else {
			System.out.println("Segunda opção satisfeita");
		}
	}
}
