public class POO {
    public static void main(String[] args) {
        //---------------Instanciando Objetos----------------------------
        User usuario1 = new User();
            usuario1.setFirstName("Grandoalto");
            usuario1.setLastName("Silvandrelio");
            usuario1.setPassword(123);
            usuario1.setLogged(false);

        User usuario2 = new User();
            usuario2.setFirstName("Pequenilda");
            usuario2.setLastName("Cindy");
            usuario2.setLogged(false);
            usuario2.setPassword(1232);




        //---------------- Saída na Tela-----------------------------


        System.out.println("Nome: " + usuario1.getFirstName() + " " + usuario1.getLastName() + " // senha: " + usuario1.getPassword() + " // " + "logado: " + "\u001B[31m" + usuario1.getLogged()+ "\u001B[0m"); // 1 Objeto instanciado

        System.out.println("Nome: " + usuario2.getFirstName() + " " + usuario2.getLastName() + " // senha: " + usuario2.getPassword() + " Logado: " + "\u001B[31m" + usuario2.getLogged() + "\u001B[0m"); // 2 Objeto instanciado
    
        usuario1.setLogged(true); // Mudando o estado do Objeto 1(usuario1)

        System.out.println("Nome: " + usuario1.getFirstName() + " " + usuario1.getLastName() + " // senha: " + usuario1.getPassword() +  " // logado: " + "\u001B[32m" + usuario1.getLogged() + "\u001B[0m");
    
    }
}
