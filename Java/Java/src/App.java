import java.util.Scanner;

public class App {
    static String password = new String("123"); // senha num BD
    static String senha = new String("123"); // senha predigitada
    
    public static void main(String[] args){

        
        ComparandoStrings1(password, senha); // resultado esperado false
        ComparandoStrings2(); // resultado esperado true
        ComparandoStrings3(password, senha); // resultado esperado true
    
    }

    static void ComparandoStrings1(String p, String s){


            System.out.println(password == senha); //O resultado será falso pois está comparando 2 espacos diferentes na memoria(suas referencias)

            System.out.println();
        }

    static void ComparandoStrings2(){

            String password = "123"; // senha do usuario no banco
            String senha = "123"; // senha predigitada
            System.out.println(password == senha); // o == está apontando que as 2 variaveis comparadas estão apontando para o mesmo espaço de memoria. o resultado pode ser verdadeiro

            System.out.println();

    }

    static void ComparandoStrings3(String p, String s){


            System.out.println(password.equals(senha)); // está comparando se o conteúdo das variaveis são iguais

            System.out.println();
        }

    }

