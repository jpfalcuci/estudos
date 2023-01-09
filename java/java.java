/* 
    java é uma linguagem orientada a objetos de propósito geral
    case sentitive
    instruções devem terminar com ;
*/

package MeuProjeto;     // pacote ao qual o arquivo pertence

// importa pacotes
import java.util.Scanner;
import java.util.Date;

public class Main {
    /** 
        este é um comentário de documentação
    */

    public static void main(String[] args) {
        // bloco principal, algorítimo contido aqui é executado

        // leitura de dados:
        Scanner leitor = new Scanner(System.in);    // import java.util.Scanner;

        int idade = leitor.nextInt();
        float cotacaoDolar = leitor.nextFloat();
        double cotacaoEuro = leitor.nextDouble();
        String nome = leitor.nextLine();
        String codigoRua = leitor.next();       // lê apenas uma palavra, não aceita espaço
        codigoRua = leitor.next().charAt(0);    // retorna o primeiro caractere da palavra


        // exibição de dados:
        System.out.print("Olá mundo");
        System.out.println("Olá mundo");    // pula pra próxima linha


        /* variáveis primitivas foram definidas junto da linguagem, armazenam valores simples
        não primitivas, podem/foram criadas após a definição da linguagem, armazenam valores mais complexos
        criação de variáveis =>      tipo nome(sempre começa com minúsculo);    ou   tipo nome = valor;
        mais comum é definir as variáveis no primeiro bloco de código */

        // primitivos
        int idade = 18;                 // números inteiros
        float cotacaoDolar = 5.0f;      // números reais
        double cotacaoEuro = 6.0d;      // números decimais
        char genero = 'M';              // uma letra, aspas simples
        byte ponto = 0;                 // numérico inteiro
        boolean estaCadastrado = false  // lógico, true e false

        // não primitivo
        String nome = "João Paulo"      // aspas duplas


        /* operadores
            +   -   /   *   %
            >   >=  <   <=  ==  !=
            &&  ||  !
        */


        // condicionais
        int media = 7;
        if(media >= 7) {
            System.out.println("Aprovado");
        } else {
            System.out.println("Reprovado");
        }

        int codigoProduto = 1;
        switch (codigoProduto) {
            case 1:
                System.out.println("Produto 1");
                break;
            case 2:
                System.out.println("Produto 2");
                break;
            default:
                // tratar erros
                break;
        }


        // estruturas de repetição

        for (int i = 0; i <= 10; i++) {
            System.out.println("O valor de i é: " + i);
        }

        int i = 0;  // quando a variável de controle precisa ser usada fora do loop, é incializada no escopo main
        for (; i <= 10; i++) {
            System.out.println("O valor de i é: " + i);
        }

        int totalAlunos = 10;
        Scanner leitorScanner = new Scanner(System.in);
        while (totalAlunos > 0) {
            String nomeAluno = leitorScanner.nextLine();
            int idadeAluno = leitorScanner.nextInt();
            System.out.println("O nome do aluno é: " + nomeAluno + "e sua idade é: " + idadeAluno);
            totalAlunos--;
        }

    }

}


/* orientação a objetos 

    polimorfismo =>
    herança =>
    abstração => trazer as informações, comportamentos do mundo real para o algoritmo
    encapusulamento => cada entidade é responsável por suas próprias informações
*/

// arquivo Pessoa.java
package IMC;

public class Pessoa {

    // atributos
    private float peso;     // informações não são acessíveis fora da classe (por padrão é public)
    private float altura;   // a classe deve disponibilizar métodos de acessos de suas informações (getters e setters)

    // construtor; sempre o mesmo nome da classe
    public Pessoa(float peso, float altura) {
        // método não obrigatório, usado quando o objeto é instânciado com valores default, ou quando precisa executar código na criação 
        this.peso = peso;
        this.altura = altura;
    }
    
    // métodos
    public float calcularIMC() {    // acesso público, retorna um float
        float imc = peso / (altura * altura);
        return imc;
    }

    public void setPeso(float peso) {
        if (peso > 0) {
            this.peso = peso;
        }
    }

    public float getPeso() {
        return peso;
    }

    public void setAltura(float altura) {
        if (altura > 0) {
            this.altura = altura;
        }
    }

    public float getAltura() {
        return altura;
    }
}

// arquivo Main.java
package IMC;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Pessoa objetoPessoa = new Pessoa();     // variável não primitiva, simulando objeto sem classe construtora definida
        float imc;

        Scanner leitor = new Scanner(System.in);

        System.out.println("Digite o peso: ");
        objetoPessoa.setPeso(leitor.nextFloat());
        System.out.println("Digite a altura: ");
        objetoPessoa.setAltura(leitor.nextFloat());

        System.out.println("IMC = " + objetoPessoa.calcularIMC());
    }
}


// herança

// arquivo Main.java
package Loja;

import java.util.Date; 

public class Main {

    public static void main(String[] args) {

        Vendedor v = new Vendedor();
        v.setNome("João");
        v.setSalario(1000.0f);
        v.setCpf("111222333-44");
        v.setDataNascimento(new Date());
        v.calcularSalario();
        v.setComissaoPorItem(10.0f);
        v.setTotalItensVendidos(10);

        System.out.println(v.getSalario());
    }
}

// arquivo Funcionario.java
package Loja;
 
import java.util.Date; 

public class Funcionario {

    private String nome;
    private String cpf;
    private Date dataNascimento;
    private float salario;

    public Funcionario() {
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public Date getDataNascimento() {
        return dataNascimento;
    }

    public void setDataNascimento(Date dataNascimento) {
        this.dataNascimento = dataNascimento;
    }

    public Double getSalario() {
        return salario;
    }

    public void setSalario(Double salario) {
        this.salario = salario;
    }

}

// arquivo Vendedor.java
package Loja;
 
import java.util.Date; 

public class Vendedor extends Funcionario {

    private int totalItensVendidos;
    private float comissaoPorItem;

    public Vendedor() {
        super();
    }

    @Override
    public Double getSalario() {
        return super.getSalario() + (this.comissaoPorItem * totalItensVendidos);
    }

    public double getComissaoPorItem() {
        return comissaoPorItem;
    }

    public void setComissaoPorItem(float comissaoPorItem) {
        this.comissaoPorItem = comissaoPorItem;
    }

    public int getTotalItensVendidos() {
        return totalItensVendidos;
    }

    public void setTotalItensVendidos(int totalItensVendidos) {
        this.totalItensVendidos = totalItensVendidos;
    }
}
