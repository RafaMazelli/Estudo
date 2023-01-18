import java.util.Scanner;

public class App {
    public static void main(String[] args){
        //TODO Auto-generated method sub
        Scanner sc = new Scanner(System.in);
        double media, nota1, nota2;
        System.out.println("Digite a nota 1:");
        nota1 = Double.parseDouble(sc.nextLine());
        System.out.println("Digite a 2 nota:");
        nota2 = Double.parseDouble(sc.nextLine());
        media = (nota1 + nota2) / 2.0;
        System.out.println("A sua media eh:" + media);
        sc.close();
    }
}
