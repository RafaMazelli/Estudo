import java.util.ArrayList;
import java.util.List;

//So, english from now on.. just because i want to :).. well, this example project is to show how an arraylist actually works, and its property is that you can add things on it after his creation, and that is what i've done down bellow,, first i created the arraylist, then i instanciated the objects using the while loop. After that i chose one of the objects created and printed, then i instantiated another object (to test and prove the array property) and printed it. 

public class POO {
    
    public static void main(String[] args){
    //----------------------CRIANDO ARRAYLIST-----------------------------

    List<User> users = new ArrayList<>();
    
    //-----------------------INSTANTIATING OBJECTS-------------------------
    int i = 0;
    while (i < 10){

        User actual = new User(false, "fulano " + i, "da Silvano " + i, 123);
        users.add(actual);
        i++;
    }
    //---------------------PRINTING AN OBJECT EXAMPLE---------------------
    
    for (User name : users){
        System.out.println(name.getFullName());
    }
    
    //System.out.println(users.get(9).getFullName());

    //-----------------INSTANTIATING ANOTHER OBJECT----------------------
    User user11 = new User(false,"sicrano " + i, "da silcrano " + i, 123);
    users.add(user11);//Adding the new user to the arraylist named users

    //---------------------------PRINTING AGAIN---------------------------
    System.out.println(users.get(10).getFullName());// Printing again the new object added to the arraylist 
    }

}

