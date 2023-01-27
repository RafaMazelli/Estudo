public class User {

    private String first_name;
    private String last_name;
    private static int count;

    //----------------------CONSTRUTOR--------------------------------

    public User(String first_name, String last_name){

        this.first_name = first_name;
        this.last_name = last_name;
    }

    //------------------------SETTER----------------------------------

    public void set_first_name(String first_name){
        this.first_name = first_name;
    }

    public void set_last_name(String last_name){
        this.last_name = last_name;
    }

    public static void set_count(int counter){
        count = count + counter;
    }

    //-----------------------GETTER------------------------------------

    public String get_first_name(){
        return first_name;
    }

    public String get_last_name(){
        return last_name;
    }

    public String get_full_name(){
        return first_name + " " + last_name;
    }
    
    public int get_count(){
        return count;
    }
}
