import java.util.Random;
import java.util.Scanner;

public class Megasena {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Este programa irá gerar 6 numeros para o sorteio da MegaSena. Digite 1-Gerar // 2-Sair.");
        String opcao = scanner.nextLine();

        if(opcao.equals("1")){
            Random generate = new Random();
            for(int i = 0; i < 6; i++){
                int number = generate.nextInt(60);
                System.out.println(number);
            }
        }else{
            System.out.println("Programa finalizado!");
        }

    }
}
