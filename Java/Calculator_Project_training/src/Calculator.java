public class Calculator {
    public static void main(String[] args) {
        int x = Integer.parseInt(args[1]);
        int y = Integer.parseInt(args[2]);

        if(args[0].equals("somar")){
            sum(x, y);
        }else if(args[0].equals("subtrair")){
            minus(x, y);
        }else if(args[0].equals("multiplicar")){
            plus(x, y);
        }else if(args[0].equals("dividir")){
            divide(x, y);
        }else{
            System.out.println("Não existe a instrução: " + args[0]);
        }
    }

    static void sum(int x, int y){
        System.out.println(x + y);
    }

    static void minus(int x, int y){
        System.out.println(x - y);
    }
    
    static void plus(int x, int y){
        System.out.println(x * y);
    }

    static void divide(int x, int y){
        System.out.println(x / y);
    }

}
