import java.util.Scanner;
import Operacoes.operadores;

public class Calculator {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o primeiro numero:");
        String numero1 = scanner.nextLine();
        int x = Integer.parseInt(numero1);
        System.out.println("Digite o segundo numero:");
        String numero2 = scanner.nextLine();
        int y = Integer.parseInt(numero2);

        System.out.println("Digite: 1-Somar // 2-Subtrair // 3-Multiplicar // 4-Dividir:");
        String operacao = scanner.nextLine();

        if(operacao.equals("1")){
            operadores.sum(x, y);
        }else if(operacao.equals("2")){
            operadores.minus(x, y);
        }else if(operacao.equals("3")){
            operadores.plus(x, y);
        }else if(operacao.equals("4")){
            operadores.divide(x, y);
        }else{
            System.out.println("Não existe a instrução: " + operacao);
        }
        scanner.close();
    }

    

}
