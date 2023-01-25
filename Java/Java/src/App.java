import java.util.Arrays;

public class App {
    //public static int[] numbersA = new int[]{2, 5, 3, 4, 55, 76 ,4 ,1};
    //public int[] numbersB = new int[]{2, 5, 3, 4, 55, 76 ,4 ,1};
    public static void main(String[] args){
        int[] numbersA = new int[]{2, 5, 3, 4, 55, 76 ,4 ,1};
        sortArray(numbersA);
        

    }
    public void comparingArray(int[] a, int[] b){
        System.out.println(Arrays.equals(a, b));
    }

    public int[] sortArray(int[] a){
        Arrays.sort(a);
        return a;
    }
}



