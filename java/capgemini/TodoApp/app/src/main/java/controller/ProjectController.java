/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controller;

import java.sql.Connection;
import java.sql.Date;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;
import model.Project;
import util.ConnectionFactory;

/**
 *
 * @author jpfal
 */
public class ProjectController {

    public void save(Project project) {

        String sql = "INSERT INTO projects "
                + "(name, description, createdAt, updatedAt) "
                + "VALUES (?, ?, ?, ?)";

        Connection conn = null;
        PreparedStatement stmt = null;

        try {
            // Estabelece a conexão com o banco de dados
            conn = ConnectionFactory.getConnection();

            // Prepara a query
            stmt = conn.prepareStatement(sql);

            // Define os valores do statement
            stmt.setString(1, project.getName());
            stmt.setString(2, project.getDescription());
            stmt.setDate(3, new Date(project.getCreatedAt().getTime()));
            stmt.setDate(4, new Date(project.getUpdatedAt().getTime()));

            // Executa a query
            stmt.execute();
        } catch (Exception e) {
            throw new RuntimeException("Erro ao salvar o projeto." + e.getMessage(), e);
        } finally {
            ConnectionFactory.closeConnection(conn, stmt);
        }
    }

    public void update(Project project) {

        String sql = "UPDATE projects SET "
                + "name = ?,"
                + "description = ?,"
                + "createdAt = ?,"
                + "updatedAt = ?"
                + "WHERE id = ?";

        Connection conn = null;
        PreparedStatement stmt = null;

        try {
            // Estabelece a conexão com o banco de dados
            conn = ConnectionFactory.getConnection();

            // Prepara a query
            stmt = conn.prepareStatement(sql);

            // Define os valores do statement
            stmt.setString(1, project.getName());
            stmt.setString(2, project.getDescription());
            stmt.setDate(3, new Date(project.getCreatedAt().getTime()));
            stmt.setDate(4, new Date(project.getUpdatedAt().getTime()));
            stmt.setInt(5, project.getId());

            // Executa a query
            stmt.execute();
        } catch (Exception e) {
            throw new RuntimeException("Erro ao atualizar o projeto." + e.getMessage(), e);
        } finally {
            ConnectionFactory.closeConnection(conn, stmt);
        }
    }

    public void removeById(int projectId) {

        String sql = "DELETE FROM projects WHERE id = ?";

        Connection conn = null;
        PreparedStatement stmt = null;

        try {
            // Estabelece a conexão com o banco de dados
            conn = ConnectionFactory.getConnection();

            // Prepara a query
            stmt = conn.prepareStatement(sql);

            // Define os valores do statement
            stmt.setInt(1, projectId);

            // Executa a query
            stmt.execute();
        } catch (Exception e) {
            throw new RuntimeException("Erro ao deletar o projeto" + e.getMessage(), e);
        } finally {
            ConnectionFactory.closeConnection(conn, stmt);
        }
    }

    public List<Project> getAll() {

        String sql = "SELECT * FROM projects";

        Connection conn = null;
        PreparedStatement stmt = null;
        ResultSet result = null;

        // Lista de tarefas que será devolvida quando a chamada do método acontecer
        List<Project> projects = new ArrayList<>();

        try {
            // Estabelece a conexão com o banco de dados
            conn = ConnectionFactory.getConnection();

            // Prepara a query
            stmt = conn.prepareStatement(sql);

            // Define os valores do statement
            // stmt.setInt(1, idProject);

            // Executa a query e armazena o valor
            result = stmt.executeQuery();

            while(result.next()) {
                Project project = new Project();

                project.setId(result.getInt("id"));
                project.setName(result.getString("name"));
                project.setDescription(result.getString("description"));
                project.setCreatedAt(result.getDate("createdAt"));
                project.setUpdatedAt(result.getDate("updatedAt"));

                projects.add(project);
            }
        } catch (Exception e) {
            throw new RuntimeException("Erro ao buscar os projetos" + e.getMessage(), e);
        } finally {
            ConnectionFactory.closeConnection(conn, stmt, result);
        }

        // Lista de tarefas que foi criada e carregada do banco de dados
        return projects;
    }
}
