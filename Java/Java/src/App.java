import java.util.Arrays;

public class App {

    public static int[] numbersA = new int[]{2, 5, 3, 4, 55, 76 ,4 ,1}; //Variable public declaration
    public static int[] numbersB = new int[]{2, 5, 3, 4, 55, 76 ,4 ,1}; //Variable public declaration

    public static void main(String[] args){
       
        sortArray(numbersA); // Using the function that i created to sort the array..(i know i could just pass the sort function from util Java's package, but i wanted to practice making my own function)
        sortArray(numbersB); //Same as previous sorting function
        System.out.println("Array 1 content: " + Arrays.toString(numbersA)); // just showing the content of the Array
        System.out.println("Array 2 content: " + Arrays.toString(numbersB));// just showing the content of the Array
        comparingArray(numbersA, numbersB); //Using the funtion that i've created to compare 2 given arrays and print ture or false if their content is equal
        comparingHashArray(numbersA, numbersB);// Using created function to compare hash arrays
        
    }
    public static void comparingArray(int[] a, int[] b){ // function that i created to compare if the content of the arrays is the same
        System.out.println("Arrays with same content: " + Arrays.equals(a, b));
    }
    public static int[] sortArray(int[] a){ // Function made to sort the given array
        Arrays.sort(a);
        return a;
    }
   public static void comparingHashArray(int[] a, int[] b){//funcion created to compare arrays

    System.out.println("Hash 1º Array: " + a);
    System.out.println("Hash 2º Array: " + b);
    System.out.println("Identical Hashs?: " + (numbersA == numbersB));
    }
}



