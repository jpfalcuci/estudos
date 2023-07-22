public class Pessoa {
	private String nomePessoa;
	private int    idadePessoa;

	@Override
	public String toString() {
		return "Pessoa [nomePessoa=" + getNomePessoa() + ", idadePessoa=" + idadePessoa + "]";
	}

	public String getNomePessoa() {
		return nomePessoa;
	}

	public void setNomePessoa(String nomePessoa) {
		this.nomePessoa = nomePessoa;
	}

	public int getIdadePessoa() {
		return idadePessoa;
	}

	public void setIdadePessoa(int idadePessoa) {
		this.idadePessoa = idadePessoa;
	}
}
