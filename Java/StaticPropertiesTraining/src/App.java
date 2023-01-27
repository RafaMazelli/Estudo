public class App {

    //So here i'm working with the concept of Static variables and how it affects on the context of the program.. When i use the static mode in a object propertie this propertie will be shared with all objects.. and when i dont will mean that each object of the class will have your own value on the propertie (not shared with everyone)
    
    
    public static void main (String[] args) {

        User rafa = new User("Rafa Mazelli", "Guiotti Sampaio");
        User tamara = new User("Tamara", "da Silva");

        User.set_count(1);
        User.set_count(1);
        User.set_count(1);
        User.set_count(2);
        User.set_count(2);
        User.set_count(2);


        System.out.println("Full name: " + rafa.get_full_name() + " // count: " + rafa.get_count());
        System.out.println("Full name: " + tamara.get_full_name() + " // count: " + tamara.get_count());
    }
}
