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
import model.Task;
import util.ConnectionFactory;

/**
 *
 * @author jpfalcuci
 */
public class TaskController {
    
    public void save(Task task) {

        String sql = "INSERT INTO tasks "
                + "(idProject, name, description, completed, notes, deadline, createdAt, updatedAt) "
                + "VALUES (?, ?, ?, ?, ?, ?, ?, ?)";

        Connection conn = null;
        PreparedStatement stmt = null;

        try {
            // Estabelece a conexão com o banco de dados
            conn = ConnectionFactory.getConnection();

            // Prepara a query
            stmt = conn.prepareStatement(sql);

            // Define os valores do statement
            stmt.setInt(1, task.getIdProject());
            stmt.setString(2, task.getName());
            stmt.setString(3, task.getDescription());
            stmt.setBoolean(4, task.isCompleted());
            stmt.setString(5, task.getNotes());
            stmt.setDate(6, new Date(task.getDeadline().getTime()));
            stmt.setDate(7, new Date(task.getCreatedAt().getTime()));
            stmt.setDate(8, new Date(task.getUpdatedAt().getTime()));

            // Executa a query
            stmt.execute();
        } catch (Exception e) {
            throw new RuntimeException("Erro ao salvar a tarefa." + e.getMessage(), e);
        } finally {
            ConnectionFactory.closeConnection(conn, stmt);
        }
    }

    public void update(Task task) {

        String sql = "UPDATE tasks SET "
                + "idProject = ?,"
                + "name = ?,"
                + "description = ?,"
                + "notes = ?,"
                + "completed = ?,"
                + "deadline = ?,"
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
            stmt.setInt(1, task.getIdProject());
            stmt.setString(2, task.getName());
            stmt.setString(3, task.getDescription());
            stmt.setString(4, task.getNotes());
            stmt.setBoolean(5, task.isCompleted());
            stmt.setDate(6, new Date(task.getDeadline().getTime()));
            stmt.setDate(7, new Date(task.getCreatedAt().getTime()));
            stmt.setDate(8, new Date(task.getUpdatedAt().getTime()));
            stmt.setInt(9, task.getId());

            // Executa a query
            stmt.execute();
        } catch (Exception e) {
            throw new RuntimeException("Erro ao atualizar a tarefa." + e.getMessage(), e);
        } finally {
            ConnectionFactory.closeConnection(conn, stmt);
        }
    }

    public void removeById(int taskId) {

        String sql = "DELETE FROM tasks WHERE id = ?";

        Connection conn = null;
        PreparedStatement stmt = null;

        try {
            // Estabelece a conexão com o banco de dados
            conn = ConnectionFactory.getConnection();

            // Prepara a query
            stmt = conn.prepareStatement(sql);

            // Define os valores do statement
            stmt.setInt(1, taskId);

            // Executa a query
            stmt.execute();
        } catch (Exception e) {
            throw new RuntimeException("Erro ao deletar a tarefa" + e.getMessage(), e);
        } finally {
            ConnectionFactory.closeConnection(conn, stmt);
        }
    }

    public List<Task> getAll(int idProject) {

        String sql = "SELECT * FROM tasks WHERE idProject = ?";

        Connection conn = null;
        PreparedStatement stmt = null;
        ResultSet result = null;

        // Lista de tarefas que será devolvida quando a chamada do método acontecer
        List<Task> tasks = new ArrayList<Task>();

        try {
            // Estabelece a conexão com o banco de dados
            conn = ConnectionFactory.getConnection();

            // Prepara a query
            stmt = conn.prepareStatement(sql);

            // Define os valores do statement
            stmt.setInt(1, idProject);

            // Executa a query e armazena o valor
            result = stmt.executeQuery();

            while(result.next()) {
                Task task = new Task();

                task.setId(result.getInt("id"));
                task.setIdProject(result.getInt("idProject"));
                task.setName(result.getString("name"));
                task.setDescription(result.getString("description"));
                task.setNotes(result.getString("notes"));
                task.setCompleted(result.getBoolean("completed"));
                task.setDeadline(result.getDate("deadline"));
                task.setCreatedAt(result.getDate("createdAt"));
                task.setUpdatedAt(result.getDate("updatedAt"));

                tasks.add(task);
            }
        } catch (Exception e) {
            throw new RuntimeException("Erro ao buscar as tarefas" + e.getMessage(), e);
        } finally {
            ConnectionFactory.closeConnection(conn, stmt, result);
        }

        // Lista de tarefas que foi criada e carregada do banco de dados
        return tasks;
    }
}
