package Cadastros;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class PessoaDao extends Dao {
	public void incluirPessoa(Pessoa p) throws Exception {
		open();
		stmt = con.prepareStatement("INSERT INTO Pessoa VALUES(?,?,?)");
		stmt.setInt(1, p.getIdPessoa());
		stmt.setString(2, p.getNomePessoa());
		stmt.setString(3, p.getEmail());
		stmt.execute();
		stmt.close();
		close();
	}

	public void alterarPessoa(Pessoa p) throws Exception {
		open();
		stmt = con.prepareStatement("UPDATE Pessoa SET nomepessoa = ?, email = ? WHERE idPessoa = ?");
		stmt.setString(1, p.getNomePessoa());
		stmt.setString(2, p.getEmail());
		stmt.setInt(3, p.getIdPessoa());
		stmt.execute();
		stmt.close();
		close();
	}

	public void excluirPessoa(Pessoa p) throws Exception {
		open();
		stmt = con.prepareStatement("DELETE FROM Pessoa WHERE idPessoa = ?");
		stmt.setInt(1, p.getIdPessoa());
		stmt.execute();
		stmt.close();
		close();
	}

	// retornando um objeto
	public Pessoa consultarPessoaIndividual(int cod) throws Exception {
			open();
			stmt = con.prepareStatement("SELECT * FROM Pessoa WHERE idPessoa = ? ");
			stmt.setInt(1, cod);
			try {
				rs = stmt.executeQuery();
			}
			catch (SQLException ex) {
				throw new Exception(ex);
				// System.out.println("Falha ao recuperar o registro. Contate TI");
			}
			finally {
				System.out.println("Fechando a conexão com banco de dados no Finally");
				close();
			}
			Pessoa p = null;
			if (rs != null) {
				if (rs.next()) {
					p = new Pessoa();
					p.setIdPessoa(rs.getInt("idPessoa"));
					p.setNomePessoa(rs.getString("nomePessoa"));
					p.setEmail(rs.getString("email"));
				}
			}
			close();
			return p;
	}

	public List<Pessoa> ListarPessoas() {
		try {
			open();
			stmt = con.prepareStatement("SELECT * FROM Pessoa");
			rs = stmt.executeQuery();
			List<Pessoa> listaPessoas = new ArrayList<>();
			while (rs.next()) {
				Pessoa p = new Pessoa();
				p.setIdPessoa(rs.getInt("idPessoa"));
				p.setNomePessoa(rs.getString("nomePessoa"));
				p.setEmail(rs.getString("email"));
				listaPessoas.add(p);
			}
			close();
			return listaPessoas;
		} catch (Exception e) {
			System.out.println(e.getMessage());
			return null;
		}
	}
}
