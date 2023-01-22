public class POO {
    public static void main(String[] args) {

        User usuario1 = new User(); // instanciando objeto da classe User
            usuario1.firstName = "Josefino"; // alterando propriedade do objeto instanciado
            usuario1.lastName = "Pequenino";// alterando propriedade do objeto instanciado
            usuario1.password = 1432;// alterando propriedade do objeto instanciado
            
        User usuario2 = new User();
            usuario2.firstName = "Marialta";
            usuario2.lastName = "Grandosvalda";
            usuario2.password = 13131;
            String fullName = usuario2.fullName();


        System.out.println("Nome: " + usuario1.firstName + " " + usuario1.lastName + " // senha: " + usuario1.password + " // " + "logado: " + usuario1.isLogged);
        System.out.println("Nome: " + usuario2.firstName + " " + usuario2.lastName + " // senha: " + usuario2.password);
    
        usuario1.setLogged(true);

        System.out.println("Nome: " + usuario1.firstName + " " + usuario1.lastName + " // senha: " + usuario1.password + " // " + usuario1.isLogged);
        System.out.println("Nome: " + usuario2.firstName + " " + usuario2.lastName + " // senha: " + usuario2.password  + " // Nome Completo: " + fullName);
    
    }
}
