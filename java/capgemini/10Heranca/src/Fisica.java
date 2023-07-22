public class Fisica extends Pessoa {
	public String cpf;
	public String identidade;

	@Override
	public String toString() {
		return "Fisica [cpf=" + cpf + ", identidade=" + identidade + ", nome=" + nome + ", situacaoPessoa=" + situacaoPessoa + "]";
	}
}
