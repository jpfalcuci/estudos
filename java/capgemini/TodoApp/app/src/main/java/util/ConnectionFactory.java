/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

/**
 *
 * @author jpfal
 */
public class ConnectionFactory {
    
//    public static final String DRIVER   = "com.mysql.jdbc.Driver"; // deprecated
    public static final String DRIVER   = "com.mysql.cj.jdbc.Driver";
    public static final String URL      = "jdbc:mysql://localhost:3306/TodoApp";
    public static final String USER     = "root";
    public static final String PASS     = "Password";
    
    // Inserir estas linhas em "dependencies" no arquivo "Build Scripts/build.gradle":
    // https://mvnrepository.com/artifact/com.mysql/mysql-connector-j
    // implementation group: 'com.mysql', name: 'mysql-connector-j', version: '8.0.33';

    public static Connection getConnection() {
        try {
            Class.forName(DRIVER);
            return DriverManager.getConnection(URL, USER, PASS);
        } catch (Exception ex) {
            throw new RuntimeException("Erro na conexão com o banco de dados", ex);
        }
    }
    
    public static void closeConnection(Connection connection) {
        try {
            if (connection != null) {
                connection.close();
            }
        } catch (Exception ex) {
            throw new RuntimeException("Erro ao fechar a conexão com o banco de dados", ex);
        }
    }

    public static void closeConnection(Connection connection, PreparedStatement statement) {
        try {
            if (connection != null) {
                connection.close();
            }
            if (statement != null) {
                statement.close();
            }
        } catch (Exception ex) {
            throw new RuntimeException("Erro ao fechar a conexão com o banco de dados", ex);
        }
    }

    public static void closeConnection(Connection connection, PreparedStatement statement, ResultSet resultSet) {
        try {
            if (connection != null) {
                connection.close();
            }
            if (statement != null) {
                statement.close();
            }
            if (resultSet != null) {
                resultSet.close();
            }
        } catch (Exception ex) {
            throw new RuntimeException("Erro ao fechar a conexão com o banco de dados", ex);
        }
    }
}
