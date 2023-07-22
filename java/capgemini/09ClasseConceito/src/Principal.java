public class Principal {
	public static void main(String[] args) throws Exception {
		// Encapsulamento
		Pessoa pes = new Pessoa();
		pes.setNomePessoa("John Snow");
		pes.setIdadePessoa(30);
		System.out.println(pes.toString());
	}
}
