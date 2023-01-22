public class POO {
    public static void main(String[] args) {

        User usuario1 = new User();
            usuario1.firstName = "Josefino";
            usuario1.lastName = "Pequenino";
            usuario1.password = 1432;
        
        User usuario2 = new User();
            usuario2.firstName = "Marialta";
            usuario2.lastName = "Grandosvalda";
            usuario2.password = 13131;

        System.out.println("Nome: " + usuario1.firstName + " " + usuario1.lastName + " // senha: " + usuario1.password);
        System.out.println("Nome: " + usuario2.firstName + " " + usuario2.lastName + " // senha: " + usuario2.password);
    }
}
